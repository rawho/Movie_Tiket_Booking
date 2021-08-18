from django.db import models
from django.contrib.auth.models import User

class Movie_Time(models.Model):
    time1 =  models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.time1

class Movie(models.Model):
    name=models.CharField(max_length=100,null=True)
    screen = models.IntegerField(default=0)
    # new
    # VOTE_TYPE = (
    #     ('Morning','9:00 AM'),
    #     ('Noon','12:00 PM'),
    #     ('Matinee','3:00 PM'),
    #     ('Evening','6:00 AM'),
    #     ('Night','9:00 PM'),
    # )
    # SCREEN_NO = (
    #     ('Screen 1','1'),
    #     ('Screen 2','2'),
    #     ('Screen 3','3'),
    #     ('Screen 4','4'),
    #     ('Screen 5','5'),
    # )
    # time = models.CharField(max_length=200,  null=True,choices=VOTE_TYPE)
    
    

    def __str__(self):
        return self.name



class Set_Timing(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,null=True)
    date1 = models.CharField(max_length=100,null=True)
    time1 = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.movie.name+" "+self.date1+" "+self.time1

class Booking(models.Model):
    set_time = models.ForeignKey(Set_Timing, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100, null=True)
    time = models.DateTimeField(null=True)
    seat = models.CharField(max_length=100,null=True)
    price = models.CharField(max_length=100,null=True)
    ticket = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.set_time.movie.name+" "

class Pending(models.Model):
    set_time = models.ForeignKey(Set_Timing, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100, null=True)
    time = models.DateTimeField(null=True)
    seat = models.CharField(max_length=100,null=True)
    price = models.CharField(max_length=100,null=True)
    ticket = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.set_time.movie.name+" "