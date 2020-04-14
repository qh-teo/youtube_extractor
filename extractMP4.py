from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    dl_prog = '0%'

    # if dl_prog != d['_percent_str']:
    #     dl_prog = d['_percent_str']
    #     print("Download progress:" + dl_prog)
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def downloadMP4(dirname,link,subtitles):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': dirname+'/%(title)s',
        'writesubtitles': subtitles,
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

# link = input("Input link: ")
# title =  input("Input name of video file: ")
# download(link)
# https://www.youtube.com/watch?v=MpYy6wwqxoo