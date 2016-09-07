from django.shortcuts import render

from django.shortcuts import render, get_object_or_404         
from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from django.core.paginator import Paginator, InvalidPage



#from . import views
from . import models
from .models import Category, Good
#urlpatterns= patterns('',
#	url(r'^(?:(?P<id>\d+)/)?$, views.index, name="index"),
#	url(r'^goods/(?P<id>)\d+)$, views.index, name="good"),


# Create your views here.
def index(request, cat_id):
    print "cat_id=", cat_id
    
    page_num = request.GET["page"]
    print "page_num=", page_num
    if cat_id == None:
        cat = Category.objects.first()
    else:
        cat = Category.objects.get(pk = cat_id)
    goods = Good.objects.filter(category = cat).order_by("name")
    return render(request, "index.html", {"category": cat, "goods":goods})

def index(request, cat_id):
    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1
    cats = Category.objects.all().order_by("name")
    if cat_id == None:
        cat = Category.objects.first()
    else:
        cat = Category.objects.get(pk = cat_id)

    test_objects_filter = Good.objects.filter(category = cat).order_by("name") 
    print  "type of test_objects_filter=", test_objects_filter
    print "type of test_objects_filter", type(test_objects_filter)
    paginator = Paginator(Good.objects.filter(category = cat).order_by("name"), 2)

    try:
        goods = paginator.page(page_num)
    except InvalidPage:
        goods = paginator.page(1)

    return render(request, "index.html", {"category": cat, "cats": cats, "goods": goods})


def good(request, good_id):
	try:
		good = Good.objects.get(pk = good_id)
	except Good.DoesNotExist:
		raise Http404
	return render(request, "good.html", {"good" : good})



    