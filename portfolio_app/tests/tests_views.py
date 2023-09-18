from django.test import TestCase
from django.urls import reverse
from portfolio_app.forms import TaskForm
from django.contrib.auth.models import User


class CreateTaskViewTestCase(TestCase):
    def test_create_task_view_form_display(self):
        response = self.client.get(reverse('create_task'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_task.html')
        self.assertIsInstance(response.context['form'], TaskForm)


class HomeViewTestCase(TestCase):
    def test_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class RegisterViewTestCase(TestCase):
    def test_register_view_post_valid(self):
        url = reverse('register')
        data = {
            'username': 'Kate123',
            'fname': 'Katerina',
            'lname': 'Funak',
            'email': 'kate@gmail.com',
            'pass1': 'admin',
            'pass2': 'admin',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='Kate123').exists())

    def test_register_view_post_invalid(self):
        url = reverse('register')
        data = {
            'username': 'Kate123',
            'fname': 'Katerinaaaaa',
            'lname': 'Funak',
            'email': 'kate@gmail.com',
            'pass1': 'admin',
            'pass2': 'admin123',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')
        self.assertFalse(User.objects.filter(username='Kate123').exists())
