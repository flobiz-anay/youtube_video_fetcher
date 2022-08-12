import time
from urllib import response
from django.conf import settings
import requests
import datetime
import asyncio
import threading
from googleapiclient.errors import HttpError

from .models import Video

def str_to_datetime(string):
  splitDateTime = string.split('T')
  return datetime.datetime.strptime(
    splitDateTime[0] + ' ' + splitDateTime[1].split('Z')[0], '%Y-%m-%d %H:%M:%S'
  )

def update_db(result):

  video_data = Video(
    video_id = result['id'],
    video_title = result['snippet']['title'],
    description = result['snippet']['description'],
    uploaded_at = result['snippet']['publishedAt'],
    video_thumbnail = result['snippet']['thumbnails']['default']['url'],
    channel_id = result['snippet']['channelId'],
    channel_title = result["snippet"]["channelTitle"]
  )

  video_data.save()

def connect_to_client(key):
  query = 'bollywood'
  try:
    search_url = settings.SEARCH_URL
    video_url = settings.VIDEO_URL
    search_params = {
      'part' : 'snippet',
      'q' : query,
      'key' : key,
      'maxResults' : 10,
      'type' : 'video'
      }

    response = requests.get(search_url, params=search_params)

    results = response.json()['items']

    video_ids = []
    for result in results:
      video_ids.append(result['id']['videoId'])
      video_params = {
        'key' : key,
        'part' : 'snippet,contentDetails',
        'id' : ','.join(video_ids),
        'maxResults' : 10
      }
    response = requests.get(video_url, params=video_params)

    final_data = response.json()['items']
    return final_data

  except HttpError as e:
    print(f'An HTTP error {e.resp.status} occurred:\n {e.content}')
    return {}


async def fetch_youtube_videos(key):
  while True:
    video_data = connect_to_client(key)
    if video_data == {}:
      return
    for data in video_data:
      try:
        print("update db")
        update_db(data)
      except Exception as e:
        print(e)
        continue
    await asyncio.sleep(300)


def scheduled_searching():
  while True:
    api_key = settings.YOUTUBE_API_KEY,
    asyncio.run(fetch_youtube_videos(api_key))

    time.sleep(10)

THREAD = threading.Thread(target=scheduled_searching)
