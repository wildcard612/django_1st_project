from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #main site
    path('', views.index, name='index'),
]