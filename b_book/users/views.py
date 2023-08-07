from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from users.form import CreateUserForm
import re
from users.models import Owner

def validate_phone_number(phone_number):
    # Define a regular expression pattern for a valid phone number
    pattern = r'^\d{10}$'

    # Check if the phone number matches the pattern
    return bool(re.match(pattern, phone_number))

# Create your views here.


def loginUser(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username OR password is incorrect')
    
    return render(request,'users/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


def signup(request):
    p_error=''
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            phno = request.POST['phno']
            if validate_phone_number(phno):
               
                user = form.save()
                Owner.objects.create(user=user,phno=phno)
                messages.success(request,f'Account created for {user.username}!')
                return redirect('login')
            else :
                p_error="phone number is not valid"
    
    return render(request,'users/signup.html',{'form':form,'p_error':p_error})

def home(request):
    pass