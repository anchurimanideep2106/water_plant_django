from django.shortcuts import render, HttpResponse, redirect
from water.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test


# Create your views here.


def home1(request):
    return render(request, 'home1.html')

def register1(request):
    if request.method=="POST":
        username=request.POST['username']
        phonenumber= request.POST['phonenumber']
        email=request.POST['email']
        password1=request.POST['password1']
        address=request.POST['address']
        User.objects.create_user(username=username, password=password1, email=email, first_name=phonenumber, last_name=address)
        return redirect('/login1')
    return render(request, 'register1.html')

def login1(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        #checking crrct credentials
        if User.objects.filter(email=email):
            U=User.objects.get(email=email)
            user = authenticate(username=U.username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/book1')
            else:
                messages.error(request, 'password incorrect')
        else:
            messages.error(request, 'email not found')
    return render(request, 'login1.html')

def signout(request):
    logout(request)
    return redirect('/')

def book1(request):
    if request.method=="POST":
        water=request.POST['water']
        coolwater=request.POST['coolwater']
        can1(water=water, cwater=coolwater).save()
        messages.success(request, 'order placed')
    return render(request, 'book1.html')

def res(request):
    s=User.objects.order_by('username')
    return render(request,"book1op.html",{'book1':s})