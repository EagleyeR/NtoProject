import json
import paho.mqtt.client as mqtt


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe('test/topic')
    else:
        print('Bad connection. Code:', rc)


def on_message(mqtt_client, userdata, msg):
    a = json.loads((msg.payload).decode('utf-8'))
    # from street.models import Apartment
    # info = Apartment.objects.get(pk=5)
    # if float(a["water_stat"]) != 0.0:
    #     info.water_stat["water_stat"].append(a["water_stat"])
    # info.save()


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
