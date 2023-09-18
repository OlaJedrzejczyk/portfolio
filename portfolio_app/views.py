from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from portfolio_app.forms import RegistrationForm
from .models import Task
from .forms import TaskForm


# Create your views here.

class HomeView(View):
    def get(self, request):

        return render(request, 'home.html')


def create_task(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        else:
            form = TaskForm()
    return render(request, 'create_task.html', {'form': form})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'delete_task.html', {'task': task})


def my_work(request):
    return render(request, 'my_work.html')


def resume(request):
    return render(request, 'resume.html')


def contact(request):
    return render(request, 'contact.html')


def register(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['fname']
            last_name = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['pass1']

            # create the user account
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            messages.success(request, "Your account has been successfully created, now you can log in")
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            # fname = user.first_name
            return render(request, "home.html")
        else:
            messages.error(request, "Wrong details")
            return redirect('login')

    return render(request, "login.html")


def user_logout(request):
    logout(request)
    # messages.success(request, "Logged out successfully")
    return redirect('home')


@login_required
def profile(request):
    return render(request, 'profile.html')
