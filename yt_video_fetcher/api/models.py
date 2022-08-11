from django.db import models

# Video Model
class Video(models.Model):
  video_id = models.CharField(max_length=250, unique=True)
  video_title = models.CharField(max_length=250)
  video_thumbnail = models.URLField()
  channel_id = models.CharField(max_length=250)
  channel_title = models.CharField(max_length=250)
  description = models.CharField(max_length=1250)
  uploaded_at = models.DateTimeField()
  
  def __str__(self):
    return self.video_title
