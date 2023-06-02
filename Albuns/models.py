from os import path
from django.db import models
from django.contrib.auth import get_user_model
from Photos.models import Photo
User = get_user_model()


# Create your models here.

class Album (models.Model):

    title = models.CharField(("Titulo"), max_length=50)
    discription = models.CharField(("Descrição"), max_length=500)
    owner = models.ForeignKey(User, verbose_name=("Dono"), on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, verbose_name=("Compartilhado com"), related_name="album_shared_with")
    create_date = models.DateTimeField(("Data de criação"), auto_now_add=True) 
    photos = models.ManyToManyField(Photo, verbose_name=("Fotos"), blank=True, null=True)
    last_modified = models.DateTimeField(("Ultima alteração"), auto_now=True) 
    delete_on_reset_day = models.BooleanField(("Deletar no dia de exclusão"))

    verbose_name = 'Album'
    verbose_name_plural = 'Albuns'

    def __str__ (self):

        return self.title
