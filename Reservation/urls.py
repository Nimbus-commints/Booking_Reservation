from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book/", views.book, name="book"),
    path("bookings/", views.bookings, name="bookings"),
    path("menu/", views.MenuItemsView.as_view(), name="menu"),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view(), name="menu-item"),
]
