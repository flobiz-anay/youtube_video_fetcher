from rest_framework import serializers

from .models import Video

class VideoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Video
    fields = ('id','video_id','video_title','description', 'uploaded_at', 'video_thumbnail')
