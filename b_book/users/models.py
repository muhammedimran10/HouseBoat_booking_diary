from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Owner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='owner')
    phno = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username