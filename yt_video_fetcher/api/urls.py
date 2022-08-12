from django.urls import path

from .views import VideosListAPI
from .services import THREAD

urlpatterns = [
    path('videos', VideosListAPI.as_view(), name="Videos"),
]

THREAD.start()
