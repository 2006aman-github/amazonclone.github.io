from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="indexPage"),
    path('cart', views.Cart, name="CartPage"),
    path('signin', views.Signin, name="SigninPage"),
    path('signin/pswd', views.Password, name="Signin-pswd-Page"),
    path('signup', views.Signup, name="SignupPage"),
    path('logout', views.Logout, name="LogoutUser"),
]