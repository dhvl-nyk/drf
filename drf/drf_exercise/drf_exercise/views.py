from django.http import HttpResponse
from drf_exercise.models.song import Song
from drf_exercise.models.song import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
import collections
from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

@cache_page(60 * 15)
def index(request):
	all_songs = Song.objects.all()
	songs = paginate(all_songs, request.GET.get('page'))
	return render_to_response('songs.html', {'songs': songs, 'request': request})

def fetch_by_tag(request):
	song_search_term = request.GET.get("tag-search")
	song_by_tag = Song.objects.filter(tags__tag_name__iexact=song_search_term.strip()).order_by('-tags__score')
	songs = paginate(song_by_tag, request.GET.get('page'))
	return render_to_response('songs.html', {'songs': songs, 'request': request})

def fetch_by_song(request):
	song_search_term = request.GET.get("song-search")
	song_by_name = Song.objects.filter(title__icontains=song_search_term.strip())
	songs = paginate(song_by_name, request.GET.get('page'))
	return render_to_response('songs.html', {'songs': songs, 'request': request})

def fetch_by_artist(request):
	song_search_term = request.GET.get("artist-search")
	songs_by_artist = Song.objects.filter(artist_name__icontains=song_search_term.strip())
	songs = paginate(songs_by_artist, request.GET.get('page'))
	return render_to_response('songs.html', {'songs': songs, 'request': request})

def show(request):
	song_id = request.GET.get("id")
	songs = Song.objects.filter(track_id=song_id)
	return render_to_response('show.html', {'songs': songs, 'request': request})

def fetch_similar_songs(request):
	song_search_term = request.GET.get("song-title")
	songs = Song.objects.filter(title__icontains=song_search_term.strip())
	return render_to_response('show.html', {'songs': songs, 'request': request})

def paginate(songs, page):
	paginator = Paginator(songs, 10)
	try:
		songs = paginator.get_page(page)
	except PageNotAnInteger:
		songs = paginator.get_page(1)
	except EmptyPage:
		songs = paginator.get_page(paginator.num_pages)
	return songs

