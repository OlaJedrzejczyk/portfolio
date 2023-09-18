from django.test import TestCase
from django.urls import reverse

class TestURLPatterns(TestCase):
    def test_home_url(self):
        response = self.client.get(reverse('home_final_app'))
        self.assertEqual(response.status_code, 200)  # Expect a successful response (HTTP 200)

    def test_form_url(self):
        response = self.client.get(reverse('form'))
        self.assertEqual(response.status_code, 200)

    def test_result_url(self):
        response = self.client.get(reverse('result'))
        self.assertEqual(response.status_code, 302)
