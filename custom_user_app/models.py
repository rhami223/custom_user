from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    displayname = models.CharField(max_length=280)
    


    def __str__(self):
        return self.username

    def get_displayname(self):
        return self.first_name + ' ' + self.last_name
