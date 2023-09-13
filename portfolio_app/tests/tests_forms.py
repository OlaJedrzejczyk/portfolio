from django.contrib.auth.models import User
from django.test import TestCase
from portfolio_app.forms import RegistrationForm


class RegistrationFormTest(TestCase):
    def test_clean_username_existing(self):
        # Create a user with the same username in the database
        existing_user = User.objects.create(username="existing_user")

        # Create a form instance with the same username
        form_data = {"username": "existing_user", "fname": "John", "lname": "Doe", "email": "john@example.com",
                     "pass1": "password", "pass2": "password"}
        form = RegistrationForm(data=form_data)

        # Ensure that clean_username raises a validation error
        self.assertFalse(form.is_valid())
        self.assertIn("Username already exists. Please choose another username", form.errors["username"])

    def test_passwords_not_matching(self):
        # Create a form instance with passwords that don't match
        form_data = {
            "username": "valid_username",
            "fname": "John",
            "lname": "Doe",
            "email": "john@example.com",
            "pass1": "password123",
            "pass2": "password456",
        }
        form = RegistrationForm(data=form_data)

        # Ensure that the form is not valid
        self.assertFalse(form.is_valid())

        # Check if the pass2 field has the expected validation error
        self.assertIn("Passwords do not match", str(form.errors))


    def setUp(self):
        # Create a user with a known email address for testing
        self.existing_user = User.objects.create_user(username="testuser", email="test@example.com",
                                                      password="testpass")

    def test_clean_email_existing(self):
        # Create a form instance with an email that is already registered
        form_data = {
            "username": "newuser",
            "fname": "John",
            "lname": "Doe",
            "email": "test@example.com",  # Email already exists in the database
            "pass1": "password123",
            "pass2": "password123",
        }
        form = RegistrationForm(data=form_data)

        # Ensure that the form is not valid
        self.assertFalse(form.is_valid())

        # Check if the 'email' field has the expected validation error
        self.assertIn("Email already registered", form.errors["email"])

    def test_clean_email_not_existing(self):
        # Create a form instance with an email that is not registered
        form_data = {
            "username": "newuser",
            "fname": "John",
            "lname": "Doe",
            "email": "new@example.com",  # Email does not exist in the database
            "pass1": "password123",
            "pass2": "password123",
        }
        form = RegistrationForm(data=form_data)

        # Ensure that the form is valid
        self.assertTrue(form.is_valid())