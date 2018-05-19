from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^oauth', views.clearRequest, name='clearRequest'),
    url(r'^userpage', views.userpage, name='userpage'),
]

