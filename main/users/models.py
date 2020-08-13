from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=60, blank=False, null=False)
    last_name = models.CharField(max_length=60, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)

    class Meta:
        verbose_name = 'User'
