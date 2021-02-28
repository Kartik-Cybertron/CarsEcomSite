from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    context={}
    # return HttpResponse("Home Page")
    return render(request,'Home.html',context)

def about(request):
    context={}
    # return HttpResponse("About Page")
    return render(request,'About.html',context)

def registrationPage(request):
    # form=UserCreationForm()
    form=CreateUserForm()

    if request.method=='POST':
        # form=UserCreationForm(request.POST)
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')


    context={'form':form}
    return render(request,'register.html',context)
    
def loginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username Or Password is incorrect')
            return redirect('login')
    context={}
    return render(request,'login.html',context)