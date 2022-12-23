import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as BaseUser

class City(models.Model):
    name=models.CharField(max_length=250, default="Chicago")
    def __str__(self) : 
       return self.name

class Room(models.Model):
    ROOM_TYPE = (
    ("1", "One Queen"), 
    ("2", "Two Queen"),
    ("3","One King"),    
    ) 

    hotel=models.ForeignKey('Hotel', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type=models.CharField(max_length=50, choices = ROOM_TYPE)
    price = models.FloatField(default=0)
    
    def __str__(self):
        return self.name + "(" + self.hotel.name + ")"

class Hotel(models.Model):
    name = models.CharField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    guest = models.IntegerField(default=0)
    check_in = models.DateTimeField(verbose_name='Check-in date')
    check_out = models.DateTimeField(verbose_name='Check-out date')
