from django.db import models

from base.models import BaseModel


class Users(BaseModel):
    name = models.CharField('Name', max_length=200)
    username = models.CharField('Username', max_length=50)
    password = models.CharField('Password', max_length=50)
