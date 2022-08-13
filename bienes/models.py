from django.db import models

from base.models import BaseModel
from users.models import Users


class Bienes(BaseModel):
    articulo = models.CharField('Artículo', max_length=255)
    descripcion = models.CharField('Artículo', max_length=255)

    usuario = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
