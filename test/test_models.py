from django.test import TestCase
from restaurant.models import MenuItem
from django.core.exceptions import ValidationError


class MenuItemModelTest(TestCase):

    def setUp(self):
        self.menu_item = MenuItem.objects.create(
            title="Test Item",
            price=10.99,
            inventory=100
        )

    def test_menu_item_creation(self):
        self.assertIsInstance(self.menu_item, MenuItem)
        self.assertEqual(self.menu_item.title, "Test Item")
        self.assertEqual(self.menu_item.price, 10.99)
        self.assertEqual(self.menu_item.inventory, 100)

    def test_get_item_method(self):
        self.assertEqual(self.menu_item.get_item(), "Test Item : 10.99")

    def test_string_representation(self):
        self.assertEqual(str(self.menu_item), self.menu_item.title)

    def test_title_max_length(self):
        max_length = self.menu_item._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_price_positive(self):
        with self.assertRaises(ValidationError):
            MenuItem.objects.create(
                title="Negative Price Item", price=-5.00, inventory=10).full_clean()

    # def test_inventory_positive(self):
    #     with self.assertRaises(ValidationError):
    #         MenuItem.objects.create(
    #             title="Negative Inventory Item", price=5.00, inventory=-10).full_clean()

    # def test_default_inventory_value(self):
    #     menu_item = MenuItem.objects.create(
    #         title="Default Inventory", price=5.00)
    #     self.assertEqual(menu_item.inventory, 0)
