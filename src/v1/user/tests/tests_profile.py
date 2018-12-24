from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status


class ProfilesTest(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')

        # URL for creating an user.
        self.create_url = reverse('user-create')

        user = User.objects.get(username='testuser')
        self.client = APIClient()
        self.client.force_authenticate(user=user)

    def test_create_profile(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """

        data = {
            'username': 'foobar',
            'email': 'foobar@example.com',
            'password': 'foobarpassword',
        }

        response = self.client.post(self.create_url, data, format='json')
        user = User.objects.latest('id')
        token = Token.objects.get(user=user)
        self.assertEquals(User.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['token'], token.key)
        self.assertFalse('password' in response.data)
