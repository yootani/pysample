from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from .forms import LoginForm

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile$', views.profile, name='profile'),

    url(r'^regist/$', views.regist, name='regist'),
    url(r'^regist_save/$', views.regist_save, name='regist_save'),

    url(r'^login/$', login,
        {'template_name': 'main/login.html', 'authentication_form': LoginForm},
        name='login'),


    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'main/index.html'},
        name='logout'),

    url(r'^activation/(?P<key>\w+)/$', views.activation, name='activation'),
]
