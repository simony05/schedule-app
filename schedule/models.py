from django.db import models
from django.contrib.auth.models import AbstractUser
import json

class User(AbstractUser):
    pass

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="schedule_user")
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=300)
    date = models.CharField(max_length=10)
    timing = models.CharField(max_length=5)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "date": self.date,
            "timing": self.timing
        }
    
    def __str__(self):
        return f"{self.title}, {self.content}, at {self.timing} on {self.date}"
