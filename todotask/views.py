from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import ToDoTasks

class todoDetail(generic.DetailView):
    model = ToDoTasks
    template_name = 'todotask/show_task.html'
    def get_context_data(self, **kwargs):
        context = super(todoDetail, self).get_context_data(**kwargs)
        return context

def todotask(request):
    if request.POST:
        username = 'houlu'#request.POST.get('username')
        title = request.POST.get('title')
        content = request.POST.get('content')
        todo = ToDoTasks(username=username, title=title, content=content)
        todo.save()
        return HttpResponseRedirect(username)
    return HttpResponse('hello')

def set_task(request):
    return render(request, 'todotask/set_task.html')
