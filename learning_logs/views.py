from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

def index(request):
    ''' main website for learning log'''
    return render(request, 'learning_logs/index.html')

def topics(request):
    '''showing all topics'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """show topic and related entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    '''add new topic'''
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    #showing empty form
    context = {'form': form}
    return render(request, "learning_logs/new_topic.html", context)