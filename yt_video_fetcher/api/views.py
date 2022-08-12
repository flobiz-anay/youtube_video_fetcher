from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination

from .models import Video
from .serializers import VideoSerializer
class VideosPagination(PageNumberPagination):
  page_size = 20
  max_page_size = 20

class VideosListAPI(generics.ListAPIView):
  queryset = Video.objects.all()
  filter_backends = (filters.SearchFilter, filters.OrderingFilter)

  search_fields = ['title']
  filter_fields = ['channelTitle']

  ordering = [
      '-uploaded_at'
  ]

  serializer_class = VideoSerializer
  pagination_class = VideosPagination
