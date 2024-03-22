from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import Testimonical,Ceo,Manager,Background
# Create your views here.


def home(request):
    obj={'test':Testimonical.objects.all(),'ceo':Ceo.objects.all(),'manager':Manager.objects.all(),'image':Background.objects.all()}
    return render(request,"inde.html")

def login(request):
    if request.method=='POST':
        name=request.POST['username']
        password=request.POST['password']
        a=auth.authenticate(username=name,password=password)
        if a is not None:
            auth.login(request,a)
            return redirect('/')
        else:
            messages.info(request,'INvalid User')
            return redirect('register')

    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        name=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword= request.POST['passwordd']
        if password==cpassword:
            if User.objects.filter(username=name).exists():
                messages.info(request,'Name already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')
            else:
                a=User.objects.create_user(username=name,email=email,password=password)
                a.save()
                print('User Registered sucessfully')
                return redirect('login')


        else:
            return redirect('register')


    return render(request,'credential.html')

def about(request):
    return render(request,'about.html')

def education(request):
    return render(request,'education.html')
def college(request):
    return render(request,'college.html')
def contact(request):
    return render(request,'contact.html')
def blog(request):
    return render(request,'blog.html')


