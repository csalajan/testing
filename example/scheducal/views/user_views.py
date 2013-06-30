from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from scheducal.serializers import UserSerializer 
from rest_framework import generics

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    if not queryset: 
        raise ObjectDoesNotExist
    serializer_class = UserSerializer
