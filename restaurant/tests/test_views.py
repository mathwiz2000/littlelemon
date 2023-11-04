from django.test import TestCase#TestCase class
from restaurant.models import *

class MenuItemTest2(TestCase):
    def setup(self):
        m1 = Menu(title = "Pizza", price="13", inventory="100")

    def get_all(self):
        return Menu.objects.all()

    def get_test_item(self):
        self.assertFalse(self.get_all() == None)