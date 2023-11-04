from django.test import TestCase#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Pizza", price=12, inventory=100)
        self.assertEqual(str(item), "Pizza : 12")