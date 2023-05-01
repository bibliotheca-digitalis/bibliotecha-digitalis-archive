import os
import json
import googleapiclient.discovery
import sys

api_key = os.environ["YOUTUBE_API_KEY"]
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
channel_id = sys.argv[1]

playlists_response = youtube.playlists().list(
    part="snippet",
    channelId=channel_id,
    maxResults=50
).execute()

playlists = playlists_response["items"]
print(json.dumps(playlists, indent=2))

