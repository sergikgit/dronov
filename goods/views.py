from django.shortcuts import render

from django.shortcuts import render, get_object_or_404         
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import RequestContext, loader
from django.core.urlresolvers import reverse



#from . import views
from . import models
from .models import Category, Good
#urlpatterns= patterns('',
#	url(r'^(?:(?P<id>\d+)/)?$, views.index, name="index"),
#	url(r'^goods/(?P<id>)\d+)$, views.index, name="good"),


# Create your views here.
def index(request, cat_id):
    print "cat_id=", cat_id
    if cat_id == None:
        cat = Category.objects.first()
    else:
        cat = Category.objects.get(pk = cat_id)
    goods = Good.objects.filter(category = cat).order_by("name")
    return render(request, "index.html", {"category": cat, "goods":goods})

def good(request, good_id):
	try:
		good = Good.objects.get(pk = good_id)
	except Good.DoesNotExist:
		raise Http404
	return render(request, "good.html", {"good" : good})



    