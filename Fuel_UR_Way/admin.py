from django.contrib import admin
from Fuel_UR_Way.models import Order
# from Fuel_UR_Way.models import Car,FuelType,CarType
# Register your models here.

# MyModels = [FuelType,CarType,Car]
MyModels = [Order]
admin.site.register(MyModels)
