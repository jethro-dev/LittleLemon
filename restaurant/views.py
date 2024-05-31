from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework import generics, viewsets
from .models import MenuItem, Booking
from rest_framework.permissions import IsAuthenticated


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
