from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    emp_id = models.CharField(max_length=5)
    emp_name = models.CharField(max_length=100)
    designation = models.ForeignKey(Position,on_delete=models.CASCADE)
    no_of_days_worked = models.IntegerField(max_length=100)
    daily_salary = models.IntegerField(max_length=100)