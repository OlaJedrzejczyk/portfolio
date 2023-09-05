from django.urls import path
from . import views
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('task_list', views.task_list, name='task_list'),
    path('create_task', views.create_task, name='create_task'),
    path('edit_task/<int:task_id>', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('my_work', views.my_work, name='my_work'),
    path('resume', views.resume, name='resume'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('profile', views.profile, name='profile'),
]