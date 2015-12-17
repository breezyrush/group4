from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from time import time
from django.utils import timezone

from django.contrib.auth.models import BaseUserManager

# CUSTOM USER AUTH
###############################################################################

class UserManager(BaseUserManager):

    def create_user(self, username, password, **kwargs):
        user = self.model(
            username=username,
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **kwargs):
        user = self.model(
            username=username,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            is_admin=True,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return UserManager

class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'

    username = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def get_full_name(self):
        return self.username
    def get_short_name(self):
        return self.username

    objects = UserManager()

###############################################################################
###############################################################################
###############################################################################
###############################################################################