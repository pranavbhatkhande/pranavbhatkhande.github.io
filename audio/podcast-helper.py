# Totally untested
# TODO(pranav) test this or something.

import os
import sys
from mutagen.mp3 import MP3

mp3filename=str(sys.argv[1])
print(mp3filename)
statinfo = os.stat(mp3filename)
size = str(statinfo.st_size)

audio = MP3(mp3filename)
length = str(audio.info.length)
 
enclosure = "<enclosure url='https://PODCAST URL/{}' length='{}' type='audio/mpeg'/>\n".format(mp3filename,size)
duration = "<itunes:duration>{}</itunes:duration>\n".format(length)

print(enclosure)
print(duration)

# Automatically add this information to the feed.xml file.

title = "new episode title"
author = "Pranav"
subtitle = "new episode subtitle"
summary = "summary of new episode"
description = "description of new episode"


class feed:
    def __init__(self,title, author, subtitle, summary, description):
        self.title = title
        self.author = author
        self.subtitle = subtitle
        self.summary = summary
        self.description = description

    def list_items(self):
        print(self.title)
        print(self.author)
        print(self.subtitle)
        print(self.summary)
        print(self.description)


u_feed = feed(title, author, subtitle, summary, description)

# arg1 is the feed object
def write_feed(feed_object, output_feed):
    feed_object.list_items()

write_feed(u_feed)
