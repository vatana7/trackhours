from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related

# Create your models here.

from teams.models import Team

class Project(models.Model):
    team = models.ForeignKey(Team, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    created_by = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def registered_time(self):
        return 0

    def num_task_todo(self):
        return 0 # self.tasks.filter(status=Task.TODO).count()