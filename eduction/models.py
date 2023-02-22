from django.db import models

# Create your models here.
# models.py

from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    # add other fields as needed
    image = models.ImageField(upload_to="media", blank=True)
    phone = models.CharField(max_length=15)
    university = models.CharField(max_length=50)
    major = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # add any additional fields you need for the teacher profile
    image = models.ImageField(upload_to="media", blank=True)
    phone = models.CharField(max_length=15)
    university = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
