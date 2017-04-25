from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^info$', views.info, name='info'),
    url(r'^info/(?P<pk>[a-zA-Z0-9]+)', views.UserInfoDetailView.as_view(), name='detail'),
]
