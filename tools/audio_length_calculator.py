# Totally untested
# TODO(pranav) test this or something.

import os
from mutagen.mp3 import MP3

        statinfo = os.stat(mp3filename)
        size = str(statinfo.st_size)

        audio = MP3(mp3filename)
        length = str(audio.info.length)

        xmlfile += "<enclosure url='https://PODCAST URL/{}' length='{}' type='audio/mpeg'/>\n".format(mp3filename,size)
        xmlfile += "<itunes:duration>{}</itunes:duration>\n".format(length)