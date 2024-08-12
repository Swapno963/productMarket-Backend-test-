from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationApiViewTest(APITestCase):

    def setUp(self):
        self.url = reverse('user_registration')
        self.user_data = {
            'first_name': 'swapno',
            'last_name': 'mondol',
            'email': 'swapno963@gmail.com',
            'password': 'strongpassword',
            'confirm_password': 'strongpassword',
        }

    def test_registration_success(self):
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertIn('Form Submission Done', response.data)

    def test_registration_invalid(self):
        self.user_data['email'] = '#'  # Invalid email
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)



class UserLoginApiViewTest(APITestCase):

    def setUp(self):
        self.url = reverse('user_login')
        self.user = User.objects.create_user(
            username='swapno_mondol', 
            first_name='swapno',
            last_name='mondol',
            email='swapno_mondol@gmail.com',
            password='strongpassword'
        )
        self.valid_payload = {
            'email': 'swapno_mondol@gmail.com',
            'password': 'strongpassword'
        }
        self.invalid_payload = {
            'email': 'janedoe@example.com',
            'password': 'wrongpassword'
        }

    def test_login_success(self):
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertIn('accessToken', response.data['token'])
        self.assertIn('refreshToken', response.data['token'])

    def test_login_failure(self):
        response = self.client.post(self.url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], 'Invalid credentials, please try again.')

    def test_login_invalid_data(self):
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
        self.assertIn('password', response.data)
