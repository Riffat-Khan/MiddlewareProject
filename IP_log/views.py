from django.http import HttpResponse
from django.views.generic import View
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

class logging_data(View):
  
  @method_decorator(ratelimit(key='ip', rate='3/m', block=True))
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)
  
  def get(self, request):
    ip_address = getattr(request, 'ip_address', 'Unknown')
    req_time = getattr(request, 'request_time', 'Unknown')

    ip_and_time = f'{ip_address}, {req_time}'
    
    return HttpResponse(ip_and_time)
