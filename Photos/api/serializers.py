from Albuns.models import Album
from rest_framework import serializers
from ..models import Photo
from Albuns.api.serializers import AlbumSerializers

class PhotoSerializers (serializers.ModelSerializer):
    album = AlbumSerializers()

    class Meta:

        model = Photo
        fields = ['title', 'album']

    