import email
from django.db import models
from django.forms import CharField

# Employee Model
class Employee(models.Model):
    employee_code=models.CharField(max_length=6, blank=False,unique=True,default='000000')
    username=models.CharField(max_length=20,blank=True)
    first_name=models.CharField(max_length=100,blank=True)  
    last_name=models.CharField(max_length=100, blank=True)
    fullname=models.CharField(max_length=200, blank=True, )  
    user_email = models.EmailField(max_length=50, blank=True, default='blank@blank.com')
    password=models.CharField(max_length=10, default="12345678")
    mobile=models.CharField(max_length=25, blank=True, unique=True)
    its_manager=models.BooleanField(default=False)
    its_supervisor=models.BooleanField(default=False)
    its_housekeeping=models.BooleanField(default=False)