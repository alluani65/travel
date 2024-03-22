from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
# def login(request):
#     if request.method=='POST':
#         name=request.POST['username']
#         password=request.POST['password']
#         a=auth.authenticate(username=name,password=password)
#         if a is not None:
#             auth.login(request,a)
#             return redirect('/')
#         else:
#             messages.info(request,'INvalid User')
#             return redirect('credential')
#     return render(request,'login.html')
#
#
#
# def register(request):
#     if request.method=='POST':
#         name=request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         cpassword= request.POST['passwordd']
#         if password==cpassword:
#             if User.objects.filter(username=name).exists():
#                 messages.info(request,'Name already taken')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,'email already taken')
#                 return redirect('register')
#             else:
#                 a=User.objects.create_user(username=name,email=email,password=password)
#                 a.save()
#                 print('User Registered sucessfully')
#                 return redirect('login')
#
#
#         else:
#             return redirect('register')
#
#
#     return render(request,'credential.html')