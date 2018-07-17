from django.db import models
from django.contrib.auth.models import AbstractUser


class Team(models.Model):
    """
    Team model
    """

    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name
        

class User(AbstractUser):
    """
    User model
    """
    team = models.ForeignKey('Team', on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.username