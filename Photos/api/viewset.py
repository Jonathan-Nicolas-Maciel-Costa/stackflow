from rest_framework import serializers, viewsets
from ..models import Photo
from .serializers import PhotoSerializers
from rest_framework.permissions import IsAuthenticated

class PhotoViewSet (viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers
