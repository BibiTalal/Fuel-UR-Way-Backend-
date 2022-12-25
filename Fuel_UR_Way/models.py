from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()


class Order (models.Model):
    # user = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="orders")
    user = models.TextField()
    carType= models.TextField()
    fuelType = models.TextField()
    litter= models.FloatField()
    address =  models.TextField()
    date = models.DateField()
    time = models.TimeField()
    price = models.FloatField()
    payed = models.TextField()
    status = models.BooleanField()
    def __str__(self):
        return self.carType


# class FuelType(models.Model):
#     name= models.TextField()
#     price= models.FloatField()
#     def __str__(self):
#         return self.name

# class CarType(models.Model):
#     brand= models.TextField()
#     def __str__(self):
#         return self.brand

# class Car(models.Model):
#     carType = models.ManyToManyField(CarType,related_name="type")
#     fuleType = models.ManyToManyField(FuelType,related_name="type")
#     user = models.TextField()
#     def __str__(self):
#         return self.user

# class Payments (models.Model):
#     method = models.TextField()
#     def __str__(self):
#         return self.method


# class Order (models.Model):
#     car= models.ManyToManyField(Car,related_name="userCar")
#     litter= models.IntegerField()
#     address =  models.TextField()
#     date = models.DateField()
#     time = models.TimeField()
#     price = models.FloatField()
#     payed = models.ManyToManyField(Payments,related_name="methods")
    
#     def __str__(self):
#         return self.litter


# class Cuisine(models.Model):
#     name = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='media/static/media', null=True)

#     def __str__(self):
#         return self.name


# class Ingredient (models.Model):
#     name = models.CharField(max_length=255)
#     # cuisine = models.ForeignKey(
#     #     Cuisine, on_delete=models.CASCADE, related_name='ingredients')

#     def __str__(self):
#         return self.name



# class Car (models.Model):
#     carType = models.IntegerField()
#     fuleType = models.IntegerField()
#     owner = models.TextField()
   
#     def __str__(self):
#         return self.owner


# class Dish (models.Model):
#     name = models.CharField(max_length=255)
#     dish = models.TextField()
#     image = models.ImageField(upload_to='media/static/media', null=True)

#     ingredients = models.ManyToManyField(
#         Ingredient, related_name='dishes')

#     cuisine = models.ForeignKey(
#         Cuisine, on_delete=models.CASCADE, related_name='dishes')

#     def __str__(self):
#         return self.name

