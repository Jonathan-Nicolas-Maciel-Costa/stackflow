from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Albuns.api.viewset import AlbumViewSet
from Photos.api.viewset import PhotoViewSet

router = DefaultRouter()
router.register(r'Album', AlbumViewSet, basename='Album')
router.register(r'Photo', PhotoViewSet, basename='Photo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
