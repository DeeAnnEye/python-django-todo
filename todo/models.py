from django.db import models

# Create your models here.


class Task(models.Model):
    task_name = models.CharField(max_length=200,null=True,blank=True)
    task_date = models.CharField(max_length=100,null=True,blank=True)
