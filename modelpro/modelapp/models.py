from django.db import models

# Create your models here.
class StudentsData(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length = 50)
    fee = models.IntegerField()
    marks = models.IntegerField()
    location = models.CharField(max_length = 50)
