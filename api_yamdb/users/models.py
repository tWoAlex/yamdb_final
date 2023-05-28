from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator


class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'admin', 'admin'
        MODERATOR = 'moderator', 'moderator'
        USER = 'user', 'user'

    username = models.CharField(max_length=150, unique=True,
                                validators=(UnicodeUsernameValidator(),))
    email = models.EmailField(unique=True)
    role = models.CharField(choices=Roles.choices, default=Roles.USER,
                            max_length=20)
    bio = models.TextField(blank=True, null=True)
    confirmation_code = models.CharField(max_length=50)

    @property
    def is_moderator(self):
        return self.role == self.Roles.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.Roles.ADMIN or self.is_superuser
