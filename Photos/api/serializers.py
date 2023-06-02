from Albuns.models import Album
from rest_framework import serializers
from ..models import Photo

class PhotoSerializers (serializers.ModelSerializer):

    class Meta:

        model = Photo
        fields = ['title']

    