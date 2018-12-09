from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework import status


class LoginTest(APITestCase):
    def setUp(self):
        """
        Ensure we can login with a new user.
        """

        self.test_user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')

        # URL for creating an user.
        self.create_url = reverse('user-login')

        user = User.objects.get(username='testuser')
        self.client = APIClient()
        self.client.force_authenticate(user=user)

    def test_login_valid_user(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_invalid_user(self):
        data = {
            'username': 'test',
            'password': 'invaliduser',
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_login_none_user_password(self):
        data = {
            'username': '',
            'password': '',
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_login_none_user(self):
        data = {
            'username': '',
            'password': 'invalidpass',
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_login_none_password(self):
        data = {
            'username': 'testuser',
            'password': '',
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_login_without_user_password(self):
        data = {

        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_without_user(self):
        data = {
            'password': 'invalidpass',
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_without_password(self):
        data = {
            'username': 'testuser',
        }

        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
