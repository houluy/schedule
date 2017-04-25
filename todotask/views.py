from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView as LV
from .models import ToDoTasks

def todoView(request, username):
    task_list = ToDoTasks.objects.filter(username=username).values()
    template_name = 'todotask/show_task.html'
    context = {
        'task_list': task_list,
        'username': username,
    }
    return render(request, template_name, context)
    
def todotask(request):
    if request.POST:
        username = 'houlu'#request.POST.get('username')
        title = request.POST.get('title')
        content = request.POST.get('content')
        todo = ToDoTasks(username=username, title=title, content=content)
        todo.save()
        return HttpResponseRedirect(username)
    return HttpResponse('hello')

def set_task(request, username):
    return render(request, 'todotask/set_task.html')

def modify_task(request, username):
    if request.POST:
        print(request.POST)
    return HttpResponseRedirect(username)
