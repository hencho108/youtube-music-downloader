from __future__ import unicode_literals
import youtube_dl
import os
from sys import argv

# Define download options
download_options = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'nocheckcertificate': True,
        'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',

        }],
}

# Create download directory if it does not exist
if not os.path.exists('downloads'):
        os.mkdir('downloads')
else:
        os.chdir('downloads')

# Download
with youtube_dl.YoutubeDL(download_options) as dl:
        with open('../' + argv[1], 'r') as f:
                for url in f:
                        dl.download([url])
