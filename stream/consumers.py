import cv2
import base64
import numpy as np
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio

class VideoStreamConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        video_link = text_data
        cap = cv2.VideoCapture(video_link)
        if not cap.isOpened():
            await self.send(text_data="Error: Unable to open video stream.")
            return

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, buffer = cv2.imencode('.jpg', gray_frame)
            frame_data = base64.b64encode(buffer).decode('utf-8')
            await self.send(text_data=frame_data)
            await asyncio.sleep(0.1)  # Adjust the delay as needed

        cap.release()
