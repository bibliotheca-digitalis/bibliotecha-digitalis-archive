import os
import googleapiclient.discovery

# Set your API key as an environment variable, or replace with your API key directly
api_key = os.environ["YOUTUBE_API_KEY"]

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

# Replace with the desired YouTube channel's ID
channel_id = "UCNvsIonJdJ5E4EXMa65VYpA"

# Fetch channel details
channel_response = youtube.channels().list(
    part="snippet,statistics",
    id=channel_id
).execute()

channel_details = channel_response["items"][0]
print("Channel Details:")
print(channel_details)

# Fetch playlists
playlists_response = youtube.playlists().list(
    part="snippet",
    channelId=channel_id,
    maxResults=50
).execute()

print("Playlists:")
for playlist in playlists_response["items"]:
    print(playlist)

# Fetch videos
videos_response = youtube.search().list(
    part="snippet",
    channelId=channel_id,
    maxResults=50,
    type="video",
    order="date"
).execute()

print("Videos:")
for video in videos_response["items"]:
    print(video)

