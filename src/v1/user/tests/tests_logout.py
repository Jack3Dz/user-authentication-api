from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework import status


class LogoutTest(APITestCase):
    def setUp(self):
        """
        Ensure we can logout when authenticated.
        """

        self.test_user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')

        # URL for creating an user.
        self.create_url = reverse('user-logout')

        user = User.objects.get(username='testuser')
        self.client = APIClient()
        self.client.force_authenticate(user=user)

    def test_logout_valid_user(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }

        response = self.client.get(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
