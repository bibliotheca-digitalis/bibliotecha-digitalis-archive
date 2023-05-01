import os
import json
import googleapiclient.discovery
import sys

api_key = os.environ["YOUTUBE_API_KEY"]
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
channel_id = sys.argv[1]

videos_response = youtube.search().list(
    part="snippet",
    channelId=channel_id,
    maxResults=50,
    type="video",
    order="date"
).execute()

videos = videos_response["items"]
print(json.dumps(videos, indent=2))
