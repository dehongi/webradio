from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/radio/$", consumers.RadioConsumer.as_asgi()),
]
