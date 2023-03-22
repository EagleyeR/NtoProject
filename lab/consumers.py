import json
from channels.consumer import AsyncConsumer
from asgiref.sync import sync_to_async

class Consumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({"type": "websocket.accept", "text": ""})

    async def websocket_receive(self, text_data):
        from .models import Lab
        full = await sync_to_async(Lab.objects.get)(pk=1)

        full_you_get = ["door", "went", "window",
                        "lux", "auto_light",
                        "pomp_works", "start_lab"]
        full.door = text_data["door"]
        full.went = text_data["went"]
        full.window = text_data["window"]
        full.lux = text_data["lux"]
        full.auto_light = text_data["auto_light"]
        full.pomp_works = text_data["pomp_works"]
        full.start_lab = text_data["start_lab"]

        full_get = {}
        full_you_for_me = ["bar", "temperature", "humidity", "heighWaterFirst", "heighWaterSecond",
                           "co2", "emission_pr", "countWater", "pumpAlert",
                           "otherGasAlert", "co2Alert", "RGB", "color", "gyroscope", "light_level",
                           "light_request"]

        for i in full_you_for_me:
            a = getattr(full, i)
            full_get[i] = a
        await self.send({
            "type": "websocket.send",
            "text": json.dumps(full_get)
        })
        full.save()

    async def websocket_disconnect(self, event):
        pass


