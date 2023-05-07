import json
import sys


arg = sys.argv[1]

js_file = open(arg, 'r')
js = json.load(js_file)

values = [
        'id',
        'webpage_url',
        'title',
        'duration',
        'duration_string',
        'age_limit',
        'channel',
        'channel_id',
        'channel_url',
        'chapters',
        'channel_follower_count',
        'view_count',
        'like_count',
        'vcodec',
        'vbr',
        'acodec',
        'audio_channels',
        'asr',
        'upload_date',
        'uploader',
        'uploader_id',
        'uploader_url',
        'tags',
        'categories',
        'thumbnail',
        'description'

]

output = ''
for attr in values:
    output += f'{attr.capitalize()}: {js.get(attr, None)}\n'

if len(output) > 4999:
    output = output[:4999]
    output = output[:output.rfind('\n')]

output = output.replace('<','')
output = output.replace('>','')

title = js['title']
channel = js['channel']

js['title'] = f'[Audio Backup] {title} | {channel}'
js['description'] = output

print(json.dumps(js, indent=4, sort_keys=True))
