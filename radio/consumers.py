import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class RadioConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket connected")  # Debug print
        await self.channel_layer.group_add("radio_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        print(f"WebSocket disconnected: {close_code}")  # Debug print
        await self.channel_layer.group_discard("radio_group", self.channel_name)

    async def receive(self, text_data):
        print(f"Received message: {text_data}")  # Debug print
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Broadcast to all connected clients
        await self.channel_layer.group_send(
            "radio_group", {"type": "broadcast_message", "message": message}
        )

    async def broadcast_message(self, event):
        print(f"Broadcasting message: {event}")  # Debug print
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))
