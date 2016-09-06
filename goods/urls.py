#coding=utf-8
from django.conf.urls import url
from . import views
from . import models
#from models import Category, Good


urlpatterns = [
    #ex: /polls/
    url(r'^(?:(?P<cat_id>\d+)/)?$', views.index, name = "index"),
    #ex: /polls/5
    url(r'^good/(?P<good_id>\d+)/$', views.good, name = 'good'),
    #ex: /polls/5/result
]



