from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from .models import member
from django.contrib.auth import logout
def home(request):
   
    template= loader.get_template("home.html")
    
    return HttpResponse(template.render())
def login(request):

    
    if request.user.is_authenticated:  # Example condition
        return redirect('/dashboard/')
    template= loader.get_template("login.html")
    return HttpResponse(template.render())
def signup(request):
    if request.user.is_authenticated:  # Example condition
        return redirect('/dashboard/')
    return render(request, 'signup.html')
# Create your views here.
def logout_view(request):
    logout(request)
    return redirect("/")
def dashboard(request):

    template= loader.get_template("Dashboard.html")
    
    return HttpResponse(template.render())