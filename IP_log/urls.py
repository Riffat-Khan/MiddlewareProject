from django.urls import path
from . import views

urlpatterns = [
  path('home/', views.logging_data.as_view(), name='logging_data'),
]