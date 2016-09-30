from django.test import TestCase
from django.test import Client

# Create your tests here.

class RootTestCase(TestCase):
    def test_root_page(self):
        c = Client()
        response = c.get('/')
        print(response.content)
        self.assertTrue("Hello, is it me you are looking for?" in response.content)
