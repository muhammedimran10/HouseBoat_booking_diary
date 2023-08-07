from django.contrib import admin
from booking import models

# Register your models here.

admin.site.register(models.Boat)
admin.site.register(models.Trip)