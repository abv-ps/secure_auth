from django.contrib.auth.models import AbstractUser
from django.db import models

from secure_auth import settings


class CustomUser(AbstractUser):
    """Custom user model."""
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
