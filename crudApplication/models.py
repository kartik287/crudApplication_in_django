from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id=models.IntegerField()
    name=models.CharField(max_length=30)
    address=models.TextField(null=True, blank=True)
    email=models.CharField(max_length=40)
    mobile_no=models.CharField(max_length=10)
    pic=models.ImageField(null=True, blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    last_updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

