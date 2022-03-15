from tkinter import Widget
from django.db import models
from django import forms

# Create your models here.
class Contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=100)
    message=models.TextField(blank=True)

    def __str__(self):
        return self.first_name