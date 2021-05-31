#Import Django

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Team(models.Model):

    #Status

    ACTIVE = 'active'
    DELETED = 'deleted'

    CHOICE_STATUS = (
        (ACTIVE, 'Active'),
        (DELETED, 'Delted')
    )


    #Field

    title = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams', on_delete=models.CASCADE)