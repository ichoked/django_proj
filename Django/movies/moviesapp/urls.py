from django.urls import path
from . import views

app_name = 'moviesapp'

urlpatterns = [
    path("", views.MoviesView.as_view(), name ='home'),
    path('movie/<slug:slug>/', views.movie_detail, name='movie_detail')
]