from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schedule_user")
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=300)
    date = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title}, {self.content}, on {self.date}"
