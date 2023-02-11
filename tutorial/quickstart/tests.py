# tests.py, at the same level as serializers.py
from rest_framework.test import APITestCase
from rest_framework import status

class UserApiTests(APITestCase):
    base_url = '/users/'

    def test_get_users(self):
        status_code = self.client.get(self.base_url).status_code
        self.assertEqual(status_code, status.HTTP_200_OK)