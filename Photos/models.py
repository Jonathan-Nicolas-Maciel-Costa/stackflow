from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from Albuns.models import Album


# Create your models here.

class Photo (models.Model):
    #album.set_photos

    title = models.CharField(("Titulo"), max_length=50)
    discription = models.CharField(("Descrição"), blank=True, null=True, max_length=500)
    photo = models.ImageField(("Foto"), upload_to='', height_field=None, width_field=None, max_length=None)

    owner = models.ForeignKey(User, verbose_name=("Dono"), on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, verbose_name=("Compartilhado com"), related_name="photo_shared_with")
    album = models.ForeignKey(Album, verbose_name=("Album"), on_delete=models.CASCADE)
    
    verbose_name = 'Photo'
    verbose_name_plural = 'Photos'
    
    def __str__ (self):
        return self.title