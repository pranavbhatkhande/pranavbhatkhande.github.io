# Prototype how to write out xml fields automatically to the feed
# pranavbhatkhande@protonmail.com
# 2021

import xml.etree.ElementTree as ET
tree = ET.parse('../feed.xml')
root = tree.getroot()

channel = root.find("channel")

item = ET.SubElement(channel, "item")
title = ET.SubElement(item, "title")
itunes_title = ET.SubElement(item, "itunes:title")
itunes_author = ET.SubElement(item, "itunes:author")
itunes_subtitle = ET.SubElement(item, "itunes:subtitle")
itunes_summary = ET.SubElement(item, "itunes:summary")
itunes_image = ET.SubElement(item, "itunes:image")
enclosure = ET.SubElement(item, "enclosure")
itunes_duration = ET.SubElement(item, "itunes:duration")
itunes_season = ET.SubElement(item,"itunes:season")

itunes_season.text = "2"

itunes_episode= ET.SubElement(item, "itunes:episode")
itunes_episodeType= ET.SubElement(item, "itunes:episodeType")
guid = ET.SubElement(item,"guid")


guid.set("isPermaLink", 'false')

pubDate= ET.SubElement(item, "pubDate")
itunes_eplicit= ET.SubElement(item, "itunes:explicit")


tree.write('output.xml')