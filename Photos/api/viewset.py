from rest_framework import serializers, viewsets
from ..models import Photo
from .serializers import PhotoSerializers

class PhotoViewSet (viewsets.ModelViewSet):

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers
