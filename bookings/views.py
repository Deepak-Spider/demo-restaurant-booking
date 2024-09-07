from django.shortcuts import render
from .models import Booking

def booking_list(request):
    bookings = Booking.objects.all().order_by('date', 'time')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

def home(request):
    return render(request, 'bookings/home.html')