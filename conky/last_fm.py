#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import requests
import re

nb_tracks = int(str(sys.argv[1]))
url = "http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=longwei&api_key=SECRET&format=json&limit=" + str(nb_tracks)
feed = requests.get(url);
if not feed.status_code == requests.codes.ok:
	print("Error fetching last.fm feed")
	exit()
for i in range(nb_tracks): 
    json = feed.json()['recenttracks']['track'][i]
    output = '${template2}' +  '{} – {} _ {}' . format(json['artist']['#text'].encode('utf-8'), json['album']['#text'].encode('utf-8'), json['name'].encode('utf-8'))
    # make a line break every 38 characters
    print(re.sub('(.{80})', '\\1 ⏎\n${template2}   ', output, 0, re.DOTALL))

