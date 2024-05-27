from django.db import models
from django.contrib.auth.models import User


# Define your models here.


class Note(models.Model):
    """Model representing a note created by a user."""
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of the Note model."""
        return self.title