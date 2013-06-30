from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'Users': reverse('user-list', request=request, format=format),
        'Work Events': reverse('workevent-list', request=request, format=format),
        'Categories': reverse('category-list', request=request, format=format),
        'Pay Periods': reverse('payperiod-list', request=request, format=format),
    })
