from django.shortcuts import render
from .forms import BookingForm
from datetime import datetime
from .models import Booking
from django.core import serializers

# Create your views here.


def index(request):
    return render(request, "index.html", {})


def book(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "book.html", context)


def bookings(request):
    date = request.GET.get("date", datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize("json", bookings)
    render(request, "bookings.html", {"bookings": booking_json})
