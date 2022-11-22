from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey


# Create your models here.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_crea = models.ForeignKey(User, on_delete=models.CASCADE)
    usuario_modifica = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract=True


class ClaseModelo2(models.Model):
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    #usuario_crea = models.ForeignKey(User, on_delete=models.CASCADE)
    #usuario_modifica = models.IntegerField(blank=True, null=True)
    usuario_crea = UserForeignKey(auto_user_add=True, related_name='+')
    usuario_modifica = UserForeignKey(auto_user_add=True, related_name='+')

    class Meta:
        abstract=True
