from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def signup(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name =request.POST['last_name']
        username =request.POST['username']
        password =request.POST['password']
        email=request.POST['email']
        confirm_password =request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
                user.save()
                print('user created')
            return redirect('/')
        else:
            messages.info(request,"password not matching")
        return redirect('welcome')
    else:
        return render(request,'signup.html')
def login(request):

    if request.method =='POST':
        username=request.POST['username']
        password= request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('http://127.0.0.1:8000/')
        else:
            messages.info(request,'invalid credentials')
            print("wrong")
            return redirect('http://127.0.0.1:8000/accounts/login')
    else:
        print('not running')
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
