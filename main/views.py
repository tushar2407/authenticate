from django.shortcuts import render
from django.contrib.auth.views import LoginView
# Create your views here.
from django.contrib.auth import authenticate, login
from main import urls
from django.views.generic import TemplateView
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#user = authenticate(username='tushar',password='tushar2001')
#if user is not None:
#    pass
#else:
#    pass
class User(LoginView):
    tepmlate_name='login.html'
    def post(self, request):
        print(request)
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        #print(type(user))
        if user is not None:
            print("hahsdhasd'''''''''''''''''''''''''''''''''''''")
            login(request,user)
            print("asdaasdasa'''''''''''''''''''''''''")
            #next_page='auth=1'
            return HttpResponseRedirect('auth=1')
        else:
            return HttpResponseRedirect('/')
            #return HttpResponseBadRequest('Not valid use')
#@login_required(login_url='/')
class Asdw(LoginRequiredMixin,TemplateView):
    login_url='/'
    template_name='asdw.html'
    redirect_field_name="redirect_to"