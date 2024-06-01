from django.test import TestCase
from restaurant.models import MenuItem
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from rest_framework import status


class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = MenuItem.objects.create(
            title="Pizza", price=12.99, inventory=10)
        self.menu_item2 = MenuItem.objects.create(
            title="Burger", price=10.99, inventory=15)
        self.menu_item3 = MenuItem.objects.create(
            title="Pasta", price=11.99, inventory=20)
        self.valid_payload = {
            'title': 'Sushi',
            'price': 13.99,
            'inventory': 5
        }
        self.invalid_payload = {
            'title': '',
            'price': 13.99,
            'inventory': 5
        }

    def test_get_all_menu_items(self):
        response = self.client.get(reverse('menu-item-list'))
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_menu_item(self):
        response = self.client.get(
            reverse('menu-item-detail', kwargs={'pk': self.menu_item1.pk}))
        menu_item = MenuItem.objects.get(pk=self.menu_item1.pk)
        serializer = MenuItemSerializer(menu_item)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_valid_menu_item(self):
        response = self.client.post(
            reverse('menu-item-list'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MenuItem.objects.count(), 4)  # 3 in setUp + 1 new

    def test_create_invalid_menu_item(self):
        response = self.client.post(
            reverse('menu-item-list'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # 3 in setUp, no new item added
        self.assertEqual(MenuItem.objects.count(), 3)

    def test_update_menu_item(self):
        response = self.client.put(
            reverse('menu-item-detail', kwargs={'pk': self.menu_item1.pk}),
            data={
                'title': 'Updated Pizza',
                'price': 15.99,
                'inventory': 8
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_menu_item = MenuItem.objects.get(pk=self.menu_item1.pk)
        self.assertEqual(updated_menu_item.title, 'Updated Pizza')
        self.assertEqual(updated_menu_item.price, 15.99)
        self.assertEqual(updated_menu_item.inventory, 8)

    def test_delete_menu_item(self):
        response = self.client.delete(
            reverse('menu-item-detail', kwargs={'pk': self.menu_item1.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MenuItem.objects.count(), 2)  # 3 in setUp - 1 deleted
