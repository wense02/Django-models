from cgitb import text
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Post(models.Model): 
      title = models.CharField(max_length=200) 
      text = models.TextField(max_length=200)   
      author = models.ForeignKey(User,default=None, on_delete=models.CASCADE)
      created_date = models.DateTimeField(default=datetime.today)
      published_date = models.DateTimeField(default=datetime.today) 


       