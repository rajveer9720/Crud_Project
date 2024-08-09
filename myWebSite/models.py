from django.db import models


# Create your models here.
class AddStudent(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, unique=True)
    password = models.CharField(max_length=80)
