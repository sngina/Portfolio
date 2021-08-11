from django.test import TestCase
from __future__ import unicode_literals

# Create your tests here.

class SimpleTest(TestCase):

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
