# from __future__ import unicode_literals
import subprocess
from yt_dlp import YoutubeDL
import win32clipboard

# youtub's format_ID:
# https://gist.github.com/AgentOak/34d47c65b1d28829bb17c24c04a0096f#dash-video
# or check formats with command:
# yt-dlp -F YT_URL
# if u wanna use certain format use clipboard => URL,ID

VLC_PATH = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"


def setPropsToYT_dl(format_ID):
    return YoutubeDL({
        'format': format_ID,
        "player_client": "android",
    })


ydl_a = setPropsToYT_dl('251')

video_formats = ['299', '137', '248', '303', '335', '399', '699']  # 1080

win32clipboard.OpenClipboard()
URL = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

if not "youtube.com/watch" in URL:
    print('Youtube_to_VLC'.center(70, '_'))
    URL = input('Enter youtube url :  ')

format_index = 0
if len(URL.split(',')) == 2:
    URL, frmt = URL.split(',')
    format_index = video_formats.index(str(frmt))

audio_url = ydl_a.extract_info(URL, download=False)['url']


def getVideoUrl(format_index):
    if format_index == 7:
        exit()
    try:
        ydl_v = setPropsToYT_dl(video_formats[format_index])
        video_url = ydl_v.extract_info(URL, download=False)['url']
        return video_url
    except:
        format_index = format_index+1
        return getVideoUrl(format_index)


video_url = getVideoUrl(format_index)
command = f'{VLC_PATH} {video_url} --input-slave={audio_url}'
subprocess.call(command)
