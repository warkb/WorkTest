from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^oauth', views.clearRequest, name='clearRequest'),
    url(r'^userpage/(?P<userid>\d+)', views.userpage, name='userpage'),
    url(r'^makeuser', views.makeuser, name='makeuser'),
]

