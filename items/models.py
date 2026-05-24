from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Lost')

class Claim(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')