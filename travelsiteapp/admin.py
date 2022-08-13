from django.contrib import admin

# Register your models here.
from .models import  User, Trip


admin.site.register([User, Trip])