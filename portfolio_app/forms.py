from django import forms
from .models import Task
from django.contrib.auth.models import User



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=20, initial="")
    fname = forms.CharField(max_length=50, initial="")
    lname = forms.CharField(max_length=50, initial="")
    email = forms.EmailField(initial="")
    pass1 = forms.CharField(widget=forms.PasswordInput, initial="")
    pass2 = forms.CharField(widget=forms.PasswordInput, initial="")

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists. Please choose another username")
        elif username and len(username) < 5:
            raise forms.ValidationError('Username must be at least 5 characters long')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already registered')
        return email

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('pass1')
        pass2 = cleaned_data.get('pass2')

        if pass1 and pass2 and pass1 != pass2:
            self.add_error('pass1', 'Passwords do not match')

        self.error_message = "Please correct the incorrect data"

        return cleaned_data
