from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    courses = models.ManyToManyField(Course, related_name='students')
