import serial
import os
import paho.mqtt.client as paho

def on_connect(client, userdata, flags, rc):
	print('Connected with result code '+str(rc))
	
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))

prev_value = 0
client = paho.Client()
ser = serial.Serial('/dev/ttyUSB0',9600)

client.on_message = on_message
client.on_connect = on_connect

client.connect('127.0.0.1', 1883, 60)

while True:
	value = 0
	value = ser.readline()
	print value
	
	if int(value) < prev_value-10 or int(value) > prev_value+10:
		prev_value = int(value)
		message = 'light:'+value
		client.publish('ubuntu/arduino',message)
	

