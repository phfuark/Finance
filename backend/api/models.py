from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    id_user = models.PositiveIntegerField(primary_key=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
