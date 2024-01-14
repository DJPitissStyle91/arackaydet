from django.urls import path
from . import views

urlpatterns = [
    path('check_data/', views.check_data, name='check_data'),
]
