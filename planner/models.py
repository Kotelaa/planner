from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=10, default='📌')
    color = models.CharField(max_length=20, default='gray')

    class Meta:
        unique_together = [('user', 'name')]
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name.capitalize()


class Tasks (models.Model):
    STATUS = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    notes = models.TextField(blank=True, null=True)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS, default='not_started')
    category = models.ManyToManyField(Category, blank=True, related_name='tasks')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', 'status']

    def __str__(self):
        return self.title.capitalize()
