#!/usr/bin/env bash

pip3 install -r requirements.txt
mkdir /usr/bin/local/rpi-cpu-temp-mqtt
cp main.py /usr/bin/local/rpi-cpu-temp-mqtt/main.py
cp rpi-cpu-temp-mqtt.service /etc/systemd/system/rpi-cpu-temp-mqtt.service
systemctl daemon-reeload
systemctl enable rpi-cpu-temp-mqtt.service
systemctl start rpi-cpu-temp-mqtt.service