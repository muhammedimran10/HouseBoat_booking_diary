from django.shortcuts import render,redirect
from datetime import datetime, timedelta,date
import calendar

from booking.models import Boat,Trip
# Create your views here.

current_date = datetime.now()
selectedDate = current_date.day

def home(request,d=0,m=0,y=0,b_id=0):
    global selectedDate
    if current_date.month == datetime.now().month and current_date.year == datetime.now().year and d==0:
        selectedDate=datetime.now().day
    else:
        selectedDate=d

    first_day = calendar.monthrange(current_date.year, current_date.month)[0]
    last_day = calendar.monthrange(current_date.year, current_date.month)[1]

    flag=0
    if current_date.month == datetime.now().month and current_date.year == datetime.now().year:
        flag=1

    boats = Boat.objects.filter(own_by=request.user)

    if b_id==0:
        s_boat=boats[0]
    else:
        s_boat= Boat.objects.get(pk=b_id)

    try:
        bookings=Trip.objects.get(boat=s_boat,date=date(y,m,d))
    except Trip.DoesNotExist:
        bookings= None
    context = {
        'bookings':bookings,
        'boats':boats,
        's_boat':s_boat,
        'm':current_date.month,
        'flag':flag,
        's_date': selectedDate,
        'year' : current_date.year,
        'months': calendar.month_name[current_date.month],
        'first_day': first_day,
        'last_day' : last_day,
        'month_days': range(1, last_day +2+first_day),
    }
    return render(request,'cal_endar/home.html',context=context)

def p_month(request):
    global current_date
    current_date = current_date - timedelta(days=30)
    return redirect(home)
     
def n_month(request):
    global current_date
    current_date = current_date + timedelta(days=30)
    return redirect(home)



