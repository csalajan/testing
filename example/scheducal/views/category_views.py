
from django.http import HttpResponse
from scheducal.models import Category
from django.utils import simplejson
from django.core import serializers
from django.views.decorators.http import require_http_methods
import datetime


@require_http_methods(['GET'])
def category_list(request):
    categories = Category.objects.all()
    data = [category.to_dict() for category in categories]
    data = simplejson.dumps(data)
    return HttpResponse(data, mimetype='application/json')

@require_http_methods(['POST'])
def category_add(request):
    name = request.POST['name']
    is_project = request.POST['is_project']
    category = Category(name=name, is_project=is_project)
    try:
        category.save()
    except:
        return HttpResponse(status=494)
    return HttpResponse(status=200)


@require_http_methods(['GET'])
def category_detail(request, pk):
    categories = Category.objects.get(pk=pk)
    data = simplejson.dumps(categories.to_dict())
    return HttpResponse(data, mimetype='application/json')



