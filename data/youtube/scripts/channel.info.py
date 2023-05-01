import os
import json
import googleapiclient.discovery
import sys

api_key = os.environ["YOUTUBE_API_KEY"]
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
channel_id = sys.argv[1]

channel_response = youtube.channels().list(
    part="snippet,statistics",
    id=channel_id
).execute()

channel_details = channel_response["items"][0]
print(json.dumps(channel_details, indent=2))
