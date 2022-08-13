from django.contrib.auth.models import AbstractUser
from django.db import models

from base.models import BaseModel


class Users(AbstractUser, BaseModel):
    name = models.CharField('Name', max_length=200)
