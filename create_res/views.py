from django.shortcuts import render,redirect
#from .models import register,update_details,Education,WorkExperience
#from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'reg.html')
def start(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
