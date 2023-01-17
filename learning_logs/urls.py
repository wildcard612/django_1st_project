from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #main site
    path('', views.index, name='index'),
    #all topics
    path('topics/', views.topics, name='topics'),
    #single topic detail page
    path('topics/(<int:topic_id>)/', views.topic, name='topic'),
]