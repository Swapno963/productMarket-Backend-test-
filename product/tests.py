from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class ProductApiTest(APITestCase):
    def setUp(self):
        # Create initial test data
        self.product1 = Product.objects.create(
            name='Product 1',
            description='description 1',
            price=30.0,
            quantity=50
        )
        self.product2 = Product.objects.create(
            name='Product 2',
            description='description 2',
            price=10.0,
            quantity=10
        )
        self.valid_payload = {
            'name': 'New Valid Product',
            'description': 'New valid product description',
            'price': 9.0,
            'quantity': 9
        }
        self.invalid_payload = {
            'name': '',
            'description': 'Invalid product',
            'price': 'invalid_price',
            'quantity': -10
        }
    
    def test_get_all_products(self):
        response = self.client.get(reverse('products-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_limited_products(self):
        response = self.client.get(reverse('products-list'),{'limit': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_product_by_id(self):
        response = self.client.get(reverse('products-detail', kwargs={'pk': self.product1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product1.name)

    def test_create_product(self):
        response = self.client.post(reverse('products-list'), data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_product(self):
        response = self.client.post(reverse('products-list'), data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_product(self):
        response = self.client.put(reverse('products-detail', kwargs={'pk': self.product1.pk}), data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.valid_payload['name'])

    def test_delete_product(self):
        response = self.client.delete(reverse('products-detail', kwargs={'pk': self.product1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 1)
