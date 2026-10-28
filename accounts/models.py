from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        STUDENT = 'STUDENT', 'Student'
        ADMIN = 'ADMIN', 'Administrator'
    
    role = models.CharField(
        max_length = 10, 
        choices = Roles.choices, 
        default = Roles.STUDENT
    )

    course = models.CharField(
        max_length = 100, 
        blank = True, 
    )

