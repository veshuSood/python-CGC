from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll_number = models.CharField()
    email = models.EmailField()
    def __str__(self):
        return self.name

   
