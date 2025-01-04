from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from .models import member
from django.contrib.auth import logout
def home(request):
   
    return render(request,"home.html")
def login(request):

    
    if request.user.is_authenticated:  # Example condition
        return redirect('/dashboard')
    else:
        template= loader.get_template("login.html")
        return HttpResponse(template.render())
def signup(request):
    if request.user.is_authenticated:  # Example condition
        return redirect('/dashboard')
    return render(request, 'signup.html')
# Create your views here.
def logout_view(request):
    logout(request)
    return redirect("home")
def dashboard(request):
    if request.user.is_authenticated:
        return render(request,"Dashboard.html")
    return redirect('/signup')

    