from django.urls import path

from movies import views

urlpatterns = [
    path(
      'movies/all', views.movies_all
    )
]
