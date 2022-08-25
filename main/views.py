from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import tutorial
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login ,logout ,authenticate
from django.contrib import messages
from .forms import NewUserForm
#authenticate to the enter password and other password 
# Create your views here.


def homepage(request):
	return render(request= request,
	template_name="main/home.html",
	context={"tutorials":tutorial.objects.all})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})
'''def homepage(request):
    return HttpResponse ("hi hi ")'''
    

def logout_request(request):
    logout(request)
    messages.info(request, "logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    if request.method=="POST":
        u= AuthenticationForm(request, data=request.POST)
        if u.is_valid():
            username=u.cleaned_data.get('username')
            password=u.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request, user)  
                messages.info(request, f"success login {username}" )
                return redirect("/")
            else:
                message.error (request, "invalid username or password ")
        else:
            message.error (request, "invalid username or password ")
           
    form=AuthenticationForm    
    return render(request=request, template_name="main/login.html",context={"form":form})