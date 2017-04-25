from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic
from .models import User_info
from .forms import User_form

def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = User_info.objects.filter(username=username).values()
        if not user:
            raise Http404('User name {} not found'.format(username))
        else:
            #Check password
            if user[0].get('password') == password:
                return HttpResponseRedirect('/todotask/{}'.format(username))
            else:
                return HttpResponse('Password Error')
    else:
        return render(request, 'login_app/login.html')

def register(request):
    return render(request, 'login_app/register.html')

def info(request):
    form = User_form(request.POST)
    if form.is_valid():
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        birthday = request.POST.get('birth')
    user_info = User_info(username=username, password=password, email=email, birth=birthday)
    user_info.save()
    return HttpResponseRedirect('info/{}'.format(username))

class UserInfoDetailView(generic.DetailView):
    model = User_info
    template_name = 'login_app/detail.html'
    def get_context_data(self, **kwargs):
        context = super(UserInfoDetailView, self).get_context_data(**kwargs)
        return context
