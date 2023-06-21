from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Company

class CompanyAPITestCase(APITestCase):
    def setUp(self):
        self.company1 = Company.objects.create(name='Company 1')
        self.company2 = Company.objects.create(name='Company 2')

    def test_list_companies(self):
        url = reverse('company-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  

    def test_retrieve_company(self):
        url = reverse('company-detail', kwargs={'pk': self.company1.id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.company1.name)

    def test_create_company(self):
        url = reverse('company-list')
        data = {'name': 'New Company'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 3) 

    def test_update_company(self):
        url = reverse('company-detail', kwargs={'pk': self.company1.id})
        data = {'name': 'Updated Company'}
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Company.objects.get(id=self.company1.id).name, 'Updated Company')

    def test_delete_company(self):
        url = reverse('company-detail', kwargs={'pk': self.company1.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Company.objects.filter(id=self.company1.id).exists())
