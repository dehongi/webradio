from django.urls import path
from . import views

urlpatterns = [
    path("", views.TrackListView.as_view(), name="track-list"),
    path("upload/", views.TrackCreateView.as_view(), name="track-upload"),
    path("play/<int:pk>/", views.play_track, name="play-track"),
]
