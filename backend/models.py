from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Department(models.Model):
    dept_name=models.CharField(max_length=100)
    def __str__(self):
        return self.dept_name
    
class Employee(models.Model):
    emp_name=models.CharField(max_length=100)
    email=models.EmailField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name="employees")

    def __str__(self):
        return self.emp_name
    

    




