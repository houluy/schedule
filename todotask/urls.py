from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^set', views.set_task, name='set'),
    url(r'^todotask', views.todotask, name='todo'),
    url(r'^(?P<pk>[a-zA-Z0-9]+)', views.todoDetail.as_view(), name='todotask'),
]
