from django.shortcuts import render,redirect
from booking.form import BoatCreationForm
from booking.models import Boat
from users.models import Owner
from django.contrib.auth.models import User

# Create your views here.

def myboats(request):
    boat = Boat.objects.filter(own_by=request.user)
    return render(request,'booking/myboats.html',{'boats':boat,'boat_id':id})

def addboat(request):
    form = BoatCreationForm()
    if request.method == 'POST':
        form = BoatCreationForm(request.POST)
        if form.is_valid():
            boat= form.save()
            boat.own_by.add(request.user)
            
            return redirect('myboats')
    return render(request,'booking/addboat.html',{'forms' : form})

def addowners(request,id):
    if request.method == 'POST':
        phno = request.POST['search']

        owner = Owner.objects.filter(phno=phno)
        return render(request,'booking/addowners.html',{'owner':owner,'boat_id':id})    
    return render(request,'booking/addowners.html')

def addowner(request,id,b_id):
    owner = User.objects.get(pk=id)
    boat = Boat.objects.get(id=b_id)
    boat.own_by.add(owner)

    return redirect('myboats',)