from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<username>[a-zA-Z0-9]+)/set', views.set_task, name='set'),
    url(r'^(?P<username>[a-zA-Z0-9]+)/modify', views.modify_task, name='modify'),
    url(r'^todotask', views.todotask, name='todo'),
    url(r'^(?P<username>[a-zA-Z0-9]+)', views.todoView, name='todotask'),
]
