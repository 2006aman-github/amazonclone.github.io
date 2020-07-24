from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request, "index.html")
def Cart(request):
    return render(request, "cart.html")
def Signin(request):
    if request.method == "POST":
        username = request.POST.get('email')
        check_in_db = User.objects.get(username=username)
        if check_in_db != None:
            return render(request, "pswd.html",{
                "username": username
            })
    return render(request, "signin.html")

def Password(request):
    if request.method == "POST":
        pswd = request.POST.get('pswd')
        username = request.POST.get('user')
        authenticate_user = authenticate(username=username, password=pswd)
        return redirect("/")

def Signup(request):
    return render(request, "signup.html")