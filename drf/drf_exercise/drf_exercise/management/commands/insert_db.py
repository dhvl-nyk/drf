#!/usr/bin/python
# encoding=utf8
from django.core.management.base import BaseCommand, CommandError

from drf_exercise.models.song import Song
from drf_exercise.models.song import Tag

from django.conf import settings
import os
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        done= 0
        not_done = 0
        json_dataset_location = settings.BASE_DIR + "/lastfm_subset"
        # import pdb; pdb.set_trace()
        for root, dirs, files in os.walk(json_dataset_location):
            for file in files:
                fname = os.path.join(root, file)
                try:
                    with open(fname, encoding='utf-8') as json_data:
                        d = json.load(json_data)
                        songs_by_scores = sorted(d["similars"], key=lambda x: x[1], reverse=True)

                        s = Song(artist_name=d["artist"],timestamp=d["timestamp"],similars=songs_by_scores ,title=d["title"],track_id=d["track_id"])
                        print (s)
                        s.save()
                        for each_tag in d["tags"]:
                            t = Tag(tag_name=each_tag[0],score=each_tag[1])
                            t.save()
                            t.songs.add(s)
                    done+=1
                except:
                    not_done+=1
                    pass
        print ("done")
        print (done)            
        print ("not_done")
        print (not_done)