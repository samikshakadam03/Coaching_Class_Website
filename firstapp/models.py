from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')

class Gallery(models.Model):
    image=models.ImageField(null=True)

class Result(models.Model):
    header=models.CharField(max_length=300)
    image=models.ImageField(null=True)

class Notice(models.Model):
    notice=models.CharField(max_length=300)
   
class Review(models.Model):
    user=models.ForeignKey(User,models.CASCADE)
    comment=models.CharField(max_length=300)
    rate=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
    
class Enquiry(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    BOARD_CHOICES = [
        ('CBSC', 'CBSC'),
        ('ISCE', 'ISCE'),
        ('SSC', 'SSC'),
        ('SEMI', 'SEMI'),
        ('COLLEGE', 'COLLEGE'),
    ]
    
    STD_CHOICES = [
        ('VII', 'VII'),
        ('VIII', 'VIII'),
        ('IX', 'IX'),
        ('X', 'X'),
        ('XI', 'XI'),
        ('XII', 'XII'),
    ]
    
    SCLTIME_CHOICES = [
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
    ]
    
    name=models.CharField(max_length=300)
    date=models.DateField(null=True, blank=True)

    email=models.CharField(max_length=300)
    mobile=models.CharField(max_length=300)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES,null=True)
    address = models.CharField(max_length=300)
    board = models.CharField(max_length=7, choices=BOARD_CHOICES,null=True)
    std = models.CharField(max_length=6, choices=STD_CHOICES,null=True)
    sclname = models.CharField(max_length=300)
    scltime = models.CharField(max_length=9, choices=SCLTIME_CHOICES,null=True)
    marks = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    message=models.CharField(max_length=300)