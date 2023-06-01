from rest_framework import serializers
from ..models import Album
#from Photos.api.serializers import PhotoSerializers

class AlbumSerializers (serializers.ModelSerializer):
    #photos = PhotoSerializers()

    class Meta:

        model = Album
        fields = ['title','discription']


        