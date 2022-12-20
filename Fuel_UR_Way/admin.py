from django.contrib import admin
from Fuel_UR_Way.models import Car
# Register your models here.

MyModels = [Car]
admin.site.register(MyModels)
