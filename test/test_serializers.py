# tests/test_serializers.py
from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer


class MenuItemSerializerTest(TestCase):
    def test_valid_data(self):
        data = {'title': 'Valid Item', 'price': 10.99, 'inventory': 100}
        serializer = MenuItemSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_price(self):
        data = {'title': 'Invalid Price Item',
                'price': -10.99, 'inventory': 100}
        serializer = MenuItemSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('price', serializer.errors)

    def test_invalid_inventory(self):
        data = {'title': 'Invalid Inventory Item',
                'price': 10.99, 'inventory': -100}
        serializer = MenuItemSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('inventory', serializer.errors)
