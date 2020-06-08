from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer
# after extended user commit
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# end
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

# extending obtainAuthToken
class getAuthToken(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        response=super(getAuthToken,self).post(request,*args,**kwargs)
        token=Token.objects.get(key=response.data['token'])
        user= User.objects.get(id=token.user_id)
        user_serializer=UserSerializer(user,many=False) # many = false is vvvv imp
        a=user_serializer.data
        return Response({'token':token.key,'user':a})