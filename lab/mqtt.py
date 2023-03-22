import json
import paho.mqtt.client as mqtt

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe('test/topic')
    else:
        print('Bad connection. Code:', rc)


def on_message(mqtt_client, userdata, msg):
    from .models import Lab
    a = json.loads((msg.payload).decode('utf-8'))
    full = Lab.objects.get(pk=1)
    full_you_for_me = ["bar", "temperature", "humidity", "heighWaterFirst", "heighWaterSecond",
                       "co2", "emission_pr", "countWater", "pumpAlert",
                       "otherGasAlert", "co2Alert", "RGB", "color", "gyroscope", "light_level",
                       "light_request"]
    for i in full_you_for_me:
        full[i] = a[i]

    # print(full.save())


MQTT_SERVER = '37.46.131.176'
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60
MQTT_USER = ''
MQTT_PASSWORD = ''

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
client.connect(
    host=MQTT_SERVER,
    port=MQTT_PORT,
    keepalive=MQTT_KEEPALIVE
)
