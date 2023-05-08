
import time
from datetime import datetime
import paho.mqtt.client as mqtt
import csv 

listOfMessages = [];
currentDay= datetime.now().date()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Logging connected with result code "+str(rc))
    
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    
    client.subscribe("sven/home/#")
    
#    client.subscribe("sven/home/Light1")
#    client.subscribe("sven/home/Light2")
#    client.subscribe("sven/home/Light3")
#    client.subscribe("sven/home/Light4")
#    client.subscribe("sven/home/Lights")
#    client.subscribe("sven/home/Lights1")
#    client.subscribe("sven/home/Lights2")
#    client.subscribe("sven/home/Lights3")
#    client.subscribe("sven/home/Lights4")
#    client.subscribe("sven/home/Lights5")
#    client.subscribe("sven/home/Light6/Status")
#    client.subscribe("sven/home/Light7/Status")
#    client.subscribe("sven/home/Light8/Status")
#    client.subscribe("sven/home/Light4/Status")
#    client.subscribe("sven/home/Light5/Status")
#    client.subscribe("sven/home/Light1/Status")
#    client.subscribe("sven/home/Light2/Status")
#    client.subscribe("sven/home/Light3/Status")
#    client.subscribe("sven/home/Light9/Status")
#    client.subscribe("sven/home/Light10/Status")
#    client.subscribe("sven/home/Light11/Status")
#    client.subscribe("sven/home/Light12/Status")
#    client.subscribe("sven/home/Light13/Status")
    
def on_message(client, userdata, msg):
    global listOfMessages
    global currentDay
    if  currentDay != datetime.now().date():
        write_to_CSV()
        currentDay = datetime.now().date()
    print(msg.topic+" "+str(msg.payload))
    listOfMessages.append((datetime.now(),msg.topic,msg.payload))
    if msg.topic == "sven/home/Logging":
        if msg.payload == "WriteOut":
            write_to_CSV()
    
    
def write_to_CSV():
    global listOfMessages
    global currentDay
    print("Writing to CSV-File")
    file_date=currentDay
    str_file_date=str(file_date)
    extension=".csv"
    file_name="./Logging/"+str_file_date+extension
    f=open(file_name,'a')
    writer = csv.writer(f)
    for message in listOfMessages:
        writer. writerow(message)
    del listOfMessages[:]
    f.close()
    
    
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()