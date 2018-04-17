# drf (import db dump)
psql -d drf_db -f back_up.sql

# Endpoint to list all entities: (list_all_songs.png)
  http://127.0.0.1:8000/

# Endpoint to list related songs for a given song, sorted accordingly: (related_song.png) 
  http://127.0.0.1:8000/fetch_similar_songs?song-title=Liquid+Time

#Endpoint to list all songs for a given tag: (search_via_tag.png)
  http://127.0.0.1:8000/fetch_by_tag?tag-search=Fusion

#Endpoint to search for songs: (song_search.png)
  http://127.0.0.1:8000/fetch_by_song?song-search=Bolero

#Endpoint to list all songs for a given artist: (search_via_artist.png)
  http://127.0.0.1:8000/fetch_by_artist?artist-search=Brand+X

#management command used to insert db
  python manage.py insert_db