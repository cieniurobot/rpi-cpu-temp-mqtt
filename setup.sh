#!/bin/bash

echo "MQTT host:"
read MQTT_HOST

echo "MQTT user:"
read MQTT_USER

echo -n "MQTT password:"
read -s MQTT_PASSWORD
echo

echo "MQTT temperature topic:"
read MQTT_TOPIC


echo "Installing requirements..."
pip3 install -r requirements.txt

echo "Setup script..."
if [ ! -d /usr/bin/rpi-cpu-temp-mqtt ]; then
  mkdir -p /usr/bin/rpi-cpu-temp-mqtt;
fi

cp main.py /usr/bin/rpi-cpu-temp-mqtt/main.py
echo "Creating service file..."
cat > /etc/systemd/system/rpi-cpu-temp-mqtt.service <<EOF
[Unit]
Description=Rpi CPU temp mqtt publisher
After=network.target

[Service]
Type=simple
Restart=always
RestartSec=5
ExecStart=/usr/bin/python3 /usr/bin/rpi-cpu-temp-mqtt/main.py -u ${MQTT_USER} -P ${MQTT_PASSWORD} -H ${MQTT_HOST} -t ${MQTT_TOPIC}

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable rpi-cpu-temp-mqtt.service
systemctl start rpi-cpu-temp-mqtt.service
echo "Setup finished!"
