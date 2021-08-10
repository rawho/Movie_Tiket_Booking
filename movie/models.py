from django.db import models
from django.contrib.auth.models import User



class Movie(models.Model):
    name=models.CharField(max_length=100,null=True)
    

    def __str__(self):
        return self.name

class Movie_Time(models.Model):
    time1 =  models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.time1

class Set_Timing(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,null=True)
    date1 = models.CharField(max_length=100,null=True)
    time1 = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.movie.name+" "+self.date11+" "+self.time1

class Booking(models.Model):
    set_time = models.ForeignKey(Set_Timing, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100, null=True)
    time = models.DateTimeField(null=True)
    seat = models.CharField(max_length=100,null=True)
    price = models.CharField(max_length=100,null=True)
    ticket = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.set_time.movie.name+" "+self.user