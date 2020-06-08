from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.models import User
# secrecy 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#@login_required(login_url='login', redirect_field_name="redirect_to")
def home(request):
    context={
        'count':User.objects.count()
    }
    return render(request, 'core/home.html', context)
def signup(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form=UserCreationForm()
    context={
        'form':form
    }
    return render(request, 'core/registration/signup.html', context)


@login_required
def secret_page(request):
    return render(request, 'core/secret_page.html')

def SecretPage(LoginRequiredMixin,TemplateView):
    template_name="core/secret_page.html"
    