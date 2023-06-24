from django.conf.urls import url
from . import views

app_name = 'trips'
urlpatterns = [
    url(r'^$', views.dashboard, name='dash'),
    url(r'^create', views.create, name='create'),
    url(r'^(?P<tid>\d+)$', views.details, name='details'),
    # url(r'^/edit', views.edit, name='edit'),
    url(r'^(?P<tid>\d+)/edit$', views.edit, name='edit'),
    url(r'^(?P<tid>\d+)/remove', views.remove, name='remove'),
    url(r'^join', views.join, name='join'),
    url(r'^leave', views.leave, name='leave'),
]