from paho.mqtt.client import Client as MC
from paho.mqtt.enums import CallbackAPIVersion
import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish

import RobotGui.core.comm.sub.coords as coords



class MQTTClient:
    def __init__(self, address="localhost", port=1883):
        self.address = address
        self.port = port
        self._connected=False
        self._mqttc = MC(CallbackAPIVersion.VERSION2)



    def _on_connect(self,client, userdata, flags, reason_code, properties):
        if reason_code.is_failure:
            print('Failed to connect. Retrying..')
        else:
            subscribe.callback(coords.callback, 'robot/coordinates')
            self._connected=True

    def setup(self,coords_slot, address = 'localhost', port = 1883):
        coords.slot = coords_slot
        self._mqttc.on_connect =self._on_connect
        self._mqttc.connect(address, port)
        self._mqttc.loop_start()


    def publish_motion(self,message):
        topic = "robot/motion"
        if self._connected:
            self._mqttc.publish(topic,message)