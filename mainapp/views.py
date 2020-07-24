from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    user = None
    if request.user.is_anonymous == False:
        user = request.user.email
        user = user.title()
        print(user)
    return render(request, "index.html", {
        "current_user": user
    })
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
        if authenticate != None:
            login(request, authenticate_user)
            return redirect("/")
        else:
            pass
            

def Signup(request):
    if request.method == "POST":
        username = request.POST.get('name')
        pswd = request.POST.get('password')
        email = request.POST.get('email')
        new_user = User.objects.create_user(username=email, password=pswd, email=username)
        new_user.save()
        return redirect("/signin")
    return render(request, "signup.html")