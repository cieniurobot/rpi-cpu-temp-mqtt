import os
import sys
import time
import argparse
import logging
import paho.mqtt.client as mqtt

last_temp = None

consoleFormatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(consoleFormatter)
consoleHandler.setLevel(logging.INFO)
logger.addHandler(consoleHandler)

logger.info("Starting...")
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="Username for mqtt connection")
parser.add_argument("-P", "--password", help="Password for mqtt connection")
parser.add_argument("-H", "--host", help="Host for mqtt connection", default="127.0.0.1")
parser.add_argument("-p", "--port", help="Port for mqtt connection", default=1883)
parser.add_argument(
    "-k",
    "--keepalive",
    help="Keepalive param for mqtt connection. Value in seconds",
    default=60
)
parser.add_argument("-t", "--topic", help="Topic for temperature publication", default="rpi_cpu_temp_mqtt/temp")
args = parser.parse_args()


def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return (temp.replace("temp=","").replace("'C", "").replace("\n", ""))


def on_connect(client, userdata, flags, rc):
    logger.info("Connected with result code: {} ".format(str(rc)))
    client.subscribe("{}/#".format(args.topic))


def on_message(client, userdata, msg):
    logger.info("New message topic: {}, payload: {}".format(msg.topic, str(msg.payload)))


client = mqtt.Client()
client.username_pw_set(args.username, args.password)
client.on_connect = on_connect
client.on_message = on_message
client.connect(args.host, args.port, args.keepalive)

while True:
    temp = measure_temp()
    if last_temp != temp:
        logger.info("Temperature update: {}".format(temp))
        last_temp = temp
        client.publish(args.topic, temp)
    time.sleep(2)
