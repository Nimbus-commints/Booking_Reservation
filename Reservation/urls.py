from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.index, name="index"),
    path("book/", views.book, name="book"),
    path("bookings/", views.bookings, name="bookings"),
    path("menu/", views.MenuItemsView.as_view(), name="menu"),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view(), name="menu-item"),
    path("api-token-auth/", obtain_auth_token, name="api-token-auth"),
]
