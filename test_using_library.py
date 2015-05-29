import paho.mqtt.client as paho

def on_connect(client, userdata, flags, rc):
	print('Connected with result code '+str(rc))
	
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	
#instantiate the client
client = paho.Client()

#callbacks
client.on_message = on_message 
client.on_connect = on_connect

#establish connection
client.connect('127.0.0.1', 1883, 60)

#publish a message
client.publish('this/topic','Awesome message using mqtt!')
