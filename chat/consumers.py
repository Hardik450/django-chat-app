# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .mongodb import messages
from datetime import datetime

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        sender = data['sender']
        message = data['message']

        # Save message in MongoDB
        messages.insert_one({
            'room': self.room,
            'sender': sender,
            'message': message,
            'timestamp': datetime.now()
        })

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'sender': sender,
                'message': message
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'sender': event['sender'],
            'message': event['message']
        }))
