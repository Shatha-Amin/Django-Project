from django.db import models
from django.contrib import admin

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()

