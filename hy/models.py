from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    meassge = models.TextField()

    def __str__(self):
        return self.name


# Create Media table (Student & Hotel )use file -Project(urls.py),settings , admin , models   and one make media folder.
class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    branch = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to="user/student")

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="acount/hotel")
    adress = models.TextField()
    c_no = models.CharField(max_length=13)
    manager = models.CharField(max_length=20)
    food = models.CharField(max_length=20)
