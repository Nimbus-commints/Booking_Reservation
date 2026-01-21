from django.shortcuts import render
from .forms import BookingForm
from datetime import datetime
from .models import Booking, Menu
from .serializer import MenuSerializer, BookingSerializer, UserSerializer
from django.core import serializers
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

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


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()  # Modelo
    serializer_class = BookingSerializer  # Serializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()  # Modelo
    serializer_class = MenuSerializer  # Serializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()  # Modelo
    serializer_class = MenuSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
