from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Activity(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=300)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.title}, {self.content}, on {self.month}/{self.day}/{self.year}"
