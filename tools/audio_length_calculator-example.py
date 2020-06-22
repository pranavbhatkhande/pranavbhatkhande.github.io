# Totally untested
# TODO(pranav) test this or something.

import os
from mutagen.mp3 import MP3

statinfo = os.stat('D:\\Podcasts\\Combustible Brains\\combustible-brains\\audio\\CBoA-Podcast-Ep3-AudioOnly.mp3')
size = str(statinfo.st_size)

audio = MP3('D:\\Podcasts\\Combustible Brains\\combustible-brains\\audio\\CBoA-Podcast-Ep3-AudioOnly.mp3')
length = str(audio.info.length)
 
xmlfile = "<enclosure url='https://PODCAST URL/{}' length='{}' type='audio/mpeg'/>\n".format('D:\\Podcasts\\Combustible Brains\\combustible-brains\\audio\\CBoA-Podcast-Ep3-AudioOnly.mp3',size)
xmlfile += "<itunes:duration>{}</itunes:duration>\n".format(length)

print(xmlfile)