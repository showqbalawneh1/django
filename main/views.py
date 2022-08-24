from django.shortcuts import render,redirect
from django.http import HttpResponse 
from .models import tutorial
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login ,logout ,authenticate
#authenticate to the enter password and other password 
# Create your views here.


def homepage(request):
	return render(request= request,
	template_name="main/home.html",
	context={"tutorials":tutorial.objects.all})

def register(request):
    if request.method=="POST":
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
                return render(request = request,
                template_name = "main/register.html",
                context={"form":form})
    else:
        form = UserCreationForm
        return render(request, "main/register.html",context={"form":form}) 
    
'''def homepage(request):
    return HttpResponse ("hi hi ")'''