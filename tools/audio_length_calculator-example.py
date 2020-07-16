# Totally untested
# TODO(pranav) test this or something.

import os
from mutagen.mp3 import MP3

statinfo = os.stat('/Users/pranav/sandboxes/pranavbhatkhande.github.io/audio/CBoA-Podcast-Ep4-AudioOnly.mp3')
size = str(statinfo.st_size)

audio = MP3('/Users/pranav/sandboxes/pranavbhatkhande.github.io/audio/CBoA-Podcast-Ep4-AudioOnly.mp3')
length = str(audio.info.length)
 
xmlfile = "<enclosure url='https://PODCAST URL/{}' length='{}' type='audio/mpeg'/>\n".format('/Users/pranav/sandboxes/pranavbhatkhande.github.io/audio/CBoA-Podcast-Ep4-AudioOnly.mp3',size)
xmlfile += "<itunes:duration>{}</itunes:duration>\n".format(length)

print(xmlfile)