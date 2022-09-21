from email import message
from django.shortcuts import render,redirect
from .forms import login_form, signup_form
from authentication_app.models import user_info
from django.contrib.auth import login,logout, authenticate

def tupphomeshop(request):
    return render(request,'base.html')


def signup_page(request):
    form = signup_form()
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect('/home/')
    return render(request,'sign_up.html',context={'form':form})

def login_page(request):
    form = login_form()
    message = ''
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"],
            )
            if user is not None:
                login(request,user)
                return redirect('/home/')
        message="LOGIN FAILED !!" \
                "Enter correct username and password"
    return render(request,'login.html',context={'form':form,'message':message})

def logout_page(request):
    logout(request)
    return redirect('/tupphomeshop/')