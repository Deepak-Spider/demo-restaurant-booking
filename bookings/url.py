from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.booking_list, name='booking_list'),
]