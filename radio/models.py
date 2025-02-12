from django.db import models


class Track(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to="tracks/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_playing = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.artist} - {self.title}"

    def toggle_play(self):
        Track.objects.all().update(is_playing=False)
        self.is_playing = True
        self.save()
