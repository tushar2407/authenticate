from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#@login_required(login_url='login', redirect_field_name="login")
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