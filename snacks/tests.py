from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class SnacksTests(TestCase):
    def test_home_page_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code , 200)

    def test_snack_list_status(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code , 200)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'home.html')

    def test_snack_list_template(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snack_list.html')


   # test
