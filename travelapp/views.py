from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import place


def demo(request):
    obj = place.objects.all()
    return render(request, "index.html", {'result': obj})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['conf_password']
        if password == conf_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")

            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname,
                                                email=email,
                                                password=password)

                user.save();


        else:
            messages.info(request, "Password not matching")
            return redirect('register')

        return redirect('login')

    return render(request, "register.html")



def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")



def logout(request):
    auth.logout(request)
    return redirect('/')