from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customuser(AbstractUser):
    pass


class Applicant(models.Model):
    user = models.OneToOneField(
        Customuser,
        on_delete=models.CASCADE,
        primary_key=True,related_name='user')
    name = models.CharField(max_length=500)
    birth_date = models.DateField()
    phone = models.CharField(max_length=11)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)