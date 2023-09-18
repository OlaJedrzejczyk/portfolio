from django.test import TestCase
from django.urls import reverse


class TestURLPatterns(TestCase):
    def test_home_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_task_list_url(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)

    def test_nonexist_url(self):
        response = self.client.get('/nonexist_url/')
        self.assertEqual(response.status_code, 404)