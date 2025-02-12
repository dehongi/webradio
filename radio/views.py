from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Track
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

# Create your views here.


class TrackListView(ListView):
    model = Track
    template_name = "radio/track_list.html"
    context_object_name = "tracks"
    ordering = ["-uploaded_at"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now_playing"] = Track.objects.filter(is_playing=True).first()
        return context


class TrackCreateView(CreateView):
    model = Track
    template_name = "radio/track_form.html"
    fields = ["title", "artist", "audio_file"]
    success_url = reverse_lazy("track-list")


def play_track(request, pk):
    try:
        track = get_object_or_404(Track, pk=pk)
        track.toggle_play()

        # Broadcast to all connected clients
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "radio_group",
            {
                "type": "broadcast_message",
                "message": {
                    "action": "play",
                    "track_id": track.id,
                    "track_url": request.build_absolute_uri(track.audio_file.url),
                    "track_title": str(track),
                },
            },
        )

        return JsonResponse({"status": "success", "track_id": track.id})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
