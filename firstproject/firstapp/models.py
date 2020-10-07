from os import lseek
from django.db import models

# Create your models here.

class Login(models.Model):
    
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40, unique=False) 
    password = models.CharField(max_length=40)
    
    class Meta:
            verbose_name_plural = "login"
            
    def __str__(self):
        return self.email
    
class Python(models.Model):
    session = models.CharField(max_length=30)
    def __str__(self):
        return self.session
    
class Student(models.Model):
    name = models.CharField(max_length=30, unique=False)
    session =  models.ForeignKey("Python", on_delete = models.PROTECT)
    
    def __str__(self):
        return self.name