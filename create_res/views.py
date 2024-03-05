from django.shortcuts import render,redirect
from .forms import RegisterForm
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

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('registration succ')
    else:
        form = RegisterForm()
    return render(request,'reg.html', {'form':form})

"""def signup(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        middlename=request.POST['middlename']
        lastname=request.POST['lastname']
        dob=request.POST['dob']
        emailaddress=request.POST['emailaddress']
        gender=request.POST['gender']
        user_name=request.POST['user_name']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        vote=register(firstname=firstname,middlename=middlename,lastname=lastname,dob=dob,emailaddress=emailaddress,gender=gender,user_name=user_name,password=password,confirmpassword=confirmpassword)
        vote.save()
    return render(request,('reg.html')) """