from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from .models import Movie

class MoviesView(View):
    """Список фильмов"""
    def get(self, request):
        movies = Movie.objects.all()
        return  render(request, "moviesapp/movie_list.html",{"movie_list": movies})

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, url=slug)
    return render(request, "moviesapp/movie_detail.html", {"movie": movie})