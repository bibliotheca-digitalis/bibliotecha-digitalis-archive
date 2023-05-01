from ytstudio import Studio
import asyncio
import os
import json
import sys
import logging

logging.basicConfig(level=logging.DEBUG)


def progress(a, b):
    a_float = a + 0.0
    b_float = b + 0.0
    ratio = a_float / b_float
    percent = ratio * 100
    rounded = round(percent, 1)
    rounded = rounded / 2
    print(f"{a}, {b}, {rounded}%", end="\r")
    pass


if os.path.exists("./login.json"):
    LOGIN_FILE = json.loads(open("./login.json", "r").read())
else:
    exit("can't run example without login json")

yt = Studio(LOGIN_FILE)

async def payload():
    try:
        await yt.login()

        dir = sys.argv[1]
        file_name = f'{dir}/audio.mp4'
        data_json = json.loads(open(f'{dir}/desc.json', 'r').read())
        
        title = data_json['title']
        description = data_json['description']
        tags = data_json['tags']
        del data_json['title']
        del data_json['description']
        del data_json['tags']
        
        data_json['monetization'] = False
        
        privacy = 'PUBLIC'
        draft = False
        extra_fields = data_json
        vid_task = await yt.uploadVideo(file_name,
                                    title=title,
                                    description=description,
                                    privacy=privacy,
                                    draft=draft,
                                    progress=progress,
                                    extra_fields=extra_fields)
        print(json.dumps(vid_task, indent=4))
        video_id = vid_task['contents']['uploadFeedbackItemRenderer']['id']['videoId']
        print(f"successfully uploaded! videoId: {video_id}")
        
        # Then edit in tags of the video
        vid_task2 = await yt.editVideo(
            video_id=video_id,
            #title="test",  # new title
            #description="test",  # new description
            #privacy="PUBLIC",  # new privacy status (PUBLIC, PRIVATE, UNLISTER)
            tags=tags,  # new tags
            #category=22,  # new category
            #thumb="./test.png",  # new thumbnail (png, jpg, jpeg, <2MB)
            #playlist=["aaaaa", "bbbbbb"],  # new playlist
            #monetization=False,  # new monetization status (True, False)
        )
        print(f"successfully edited video tags: {vid_task2}")
    except Exception as e:
        print(f"An error occurred: {e}")
        

async def main():
    await payload()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
