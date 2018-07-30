# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.test import APIRequestFactory, APITestCase, APIClient, URLPatternsTestCase
from rest_framework import status
from django.urls import reverse

class PizzaTests(APITestCase):


    def test_create_order(self):
        data = {'pizza_id': '56565656', 'pizza_size': '30cm', 'costumer_name': 'Mr Tester',
        'costumer_address': 'Tester lane 5'}
        client = APIClient()
        client.post('/pizza/', data, format='json')
        response = self.client.get('/pizza/56565656/')
        self.assertEqual(response.data, {'pizza_id': '56565656', 'pizza_size': '30cm', 'costumer_name': 'Mr Tester',
                                         'costumer_address': 'Tester lane 5'})
        our_url = reverse('pizza-list')
        response = self.client.get(our_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        print "it is ", len(response.data)
        client.delete('/pizza/56565656/')
        self.assertEqual(len(response.data), 1)
        second_response = self.client.get(our_url, format='json')
        self.assertEqual(len(second_response.data), 0)
