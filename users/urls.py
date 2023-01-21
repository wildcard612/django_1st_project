"""adress patterns for app users"""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    url('register/', views.register, name='register'),
]