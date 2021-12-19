from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.

class Message(models.Model):
    name=CharField(max_length=30)
    email=CharField(max_length=40)
    contact_no=CharField(max_length=10)
    message=TextField()

    def __str__(self):
        return self.name