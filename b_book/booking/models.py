from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Boat(models.Model):
    name = models.CharField( max_length=50)
    own_by = models.ManyToManyField(User,related_name='boat')

    def __str__(self):
        return self.name

class Trip(models.Model):

    DAY = 'day'
    OVERNIGHT = 'overnight'
    NIGHTSTAY = 'nightstay'

    TRIP_TYPE=(
        (DAY , 'day'),
        (OVERNIGHT ,'overnight'),
        (NIGHTSTAY ,'nightstay')
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='trip')
    c_name = models.CharField(max_length=50)
    boat = models.ForeignKey(Boat,related_name='trip',on_delete=models.CASCADE)
    t_type= models.CharField(max_length=20, choices=TRIP_TYPE,default=OVERNIGHT)
    no_of_guest = models.IntegerField
    ph_no = models.CharField(max_length=12)
    rate = models.IntegerField
    rooms = models.IntegerField(blank=True)
    note = models.CharField(max_length=250)
    date = models.DateField(null=True)

    def __str__(self):
        return self.t_type