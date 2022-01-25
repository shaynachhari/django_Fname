from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    meassge = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=45)
    roll = models.IntegerField()
    email = models.EmailField()
    password = models.IntegerField()
    phone = models.CharField(max_length=13)
    gender = models.CharField(max_length=20, null=True)
    meassge = models.TextField()

    def __str__(self):
        return self.name
