from django.shortcuts import render

def index(request):
    ''' main website for learning log'''
    return render(request, 'learning_logs/index.html')