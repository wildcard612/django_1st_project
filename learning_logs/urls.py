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
    #website for new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    #wesite for adding new entries
    path('new_entry/<int:topic_id>)/', views.new_entry, name='new_entry'),
    #website for editing entries
    path('edit_entry/<int:entry_id>)/', views.edit_entry, name='edit_entry'),
]