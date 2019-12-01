# coding=utf-8
import ssl
import requests
from pydub import AudioSegment
from bs4 import BeautifulSoup


import time

ssl._create_default_https_context = ssl._create_unverified_context
# open the show list page
r = requests.get(
    "https://mp.weixin.qq.com/s/USkByuOUJZuBhQYAENCA4Q"
)
html = r.text
soup = BeautifulSoup(html,'lxml')
seq = 1
files=[]
for child in soup.descendants:
    if child.name=='p' and child.mpvoice is not None:
        #print(child)
        audio_link = child.mpvoice['voice_encode_fileid']
        audio_link = 'http://res.wx.qq.com/voice/getvoice?mediaid=' + audio_link
        r_audio = requests.get(audio_link)
        file_name = str(seq)+'.mp3'
        with open(file_name, 'wb') as f:
            f.write(r_audio.content)
        seq += 1
        files.append(file_name)
merge_sound = AudioSegment.empty()
for file in files:
    sound = AudioSegment.from_file(file, format="mp3")
    merge_sound += sound
merge_sound.export("merge.mp3", format="mp3")





