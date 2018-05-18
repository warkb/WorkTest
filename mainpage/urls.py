from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dev/Login\?', views.getUser, name='getUser'),
    url(r'^vk', views.clearRequest, name='clearRequest'),
]

