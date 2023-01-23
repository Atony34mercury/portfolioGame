from django.db import models

from datetime import time

class Room(models.Model):
    name = models.CharField(max_length=200)
    floor = models.IntegerField(default=0)
    room_number = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.name} at {self.floor} with {self.room_number}"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
