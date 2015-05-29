import os

os.system('mosquitto_pub -d -t ubuntu/arduino -m "calling from python!"')
