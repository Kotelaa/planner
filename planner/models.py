from django.db import models
from django.contrib.auth.models import User

class Tasks (models.Model):
    STATUS = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS, default='not_started')
    category = models.CharField(max_length=50, default='No category')

