from django.db import models
# Create your models here.
class Student(models.Model):
    stud_name = models.CharField(max_length=200)
    Gender=models.CharField(max_length=200)
    Department=models.CharField(max_length=200)
    email=models.EmailField()
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    cridet_hour=models.CharField(max_length=200)
    description=models.TextField()
    course_title=models.CharField(max_length=200)
