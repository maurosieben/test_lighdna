#!/usr/bin/python

import paho.mqtt.client as mqtt
from time import gmtime, strftime
import os

prog_dir = os.path.dirname(os.path.abspath(__file__))

def on_connect(client, userdata, rc):
	print("\n[MQTT]Conectado ao Broker: 192.168.0.100\n")
	client.subscribe("lights/+/status")

def on_message(client, userdata, msg):
	data = msg.payload.split(' ')
	csvF = open("%s/registry.csv" %prog_dir,'a+')
	lastTAG = "0"

	if data[0] == "Hello": #Hello - Inicio de mensagem MQTT que so acontece no boot da lum. no broker
		register = 0 #Indicativo se a lum. ja foi cadastrada anteriomente no .csv
		for line in csvF:
			if line[0] == data[3]:
				register = 1

		if register == 0: #Se ela nao foi cadastrada ate o momento, cadastra no .csv e informa o arquivo da interface
			csvF.write(data[3]+",\n")
			csvF.close()
			
			print '\nNova luminaria detectada na rede:\n'+'HW-ID:['+data[3]+'] '
		else:
			print "Luminaria ja cadastrada reiniciou:\n"+'HW-ID:['+data[3]+']\n'
			csvF.close()

def make_con():
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect("192.168.0.100", 1883, 60)
	client.loop_forever()

if __name__ == "__main__":
	make_con()
