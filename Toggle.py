
import time
import paho.mqtt.client as mqtt


state1 = False;
state2 = False;
state3 = False;
state4 = False;
state5 = False;
state6 = False;
state7 = False;
state8 = False;
state9 = False;
state10 = False;
state11 = False;
state12 = False;
state13 = False;
state14 = False;
state15 = False;
state16 = False;
state17 = False;
state18 = False;
state19 = False;
state20 = False;
state21 = False;
state22 = False;
state23 = False;
state24 = False;
state25 = False;
state26 = False;


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    state1 = False
    state2 = False
    state3 = False

    
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("sven/home/Light1")
    client.subscribe("sven/home/Light2")
    client.subscribe("sven/home/Light3")
    client.subscribe("sven/home/Light4")
    client.subscribe("sven/home/Lights")
    client.subscribe("sven/home/Lights0")
    client.subscribe("sven/home/Lights1")
    client.subscribe("sven/home/Lights2")
    client.subscribe("sven/home/Lights3")
    client.subscribe("sven/home/Lights4")
    client.subscribe("sven/home/Lights5")
    client.subscribe("sven/home/Lights6")
    client.subscribe("sven/home/Lights7")
    client.subscribe("sven/home/Lights8")
    client.subscribe("sven/home/Lights9")
    client.subscribe("sven/home/Light6/Status")
    client.subscribe("sven/home/Light7/Status")
    client.subscribe("sven/home/Light8/Status")
    client.subscribe("sven/home/Light4/Status")
    client.subscribe("sven/home/Light5/Status")
    client.subscribe("sven/home/Light1/Status")
    client.subscribe("sven/home/Light2/Status")
    client.subscribe("sven/home/Light3/Status")
    client.subscribe("sven/home/Light9/Status")
    client.subscribe("sven/home/Light10/Status")
    client.subscribe("sven/home/Light11/Status")
    client.subscribe("sven/home/Light12/Status")
    client.subscribe("sven/home/Light13/Status")
    
    client.subscribe("sven/home/Light14")
    client.subscribe("sven/home/Light15")
    client.subscribe("sven/home/Light16")
    client.subscribe("sven/home/Light17")
    client.subscribe("sven/home/Light18")
    client.subscribe("sven/home/Light19")
    client.subscribe("sven/home/Light20")
    client.subscribe("sven/home/Light21")
    client.subscribe("sven/home/Light22")
    client.subscribe("sven/home/Light23")
    client.subscribe("sven/home/Light24")
    client.subscribe("sven/home/Light25")
    client.subscribe("sven/home/Light26")
    
def on_message(client, userdata, msg):
    global state1
    global state2
    global state3
    global state4
    global state5
    global state6
    global state7
    global state8
    global state9
    global state10
    global state11
    global state12
    global state13
    global state14
    global state15
    global state16
    global state17
    global state18
    global state19
    global state20
    global state21
    global state22
    global state23
    global state24
    global state25
    global state26

    print(msg.topic+" "+str(msg.payload))
    if msg.topic == "sven/home/Lights":
        if msg.payload[1] == "N":
            client.publish("sven/home/Light1","ON")
            client.publish("sven/home/Light2","ON")
            client.publish("sven/home/Light3","ON")
            state1 = True;
            state2 = True;
            state3 = True;
        if msg.payload[1] == "F":
            client.publish("sven/home/Light1","OFF")
            client.publish("sven/home/Light2","OFF")
            client.publish("sven/home/Light3","OFF")
            state1 = False;
            state2 = False;
            state3 = False;
        elif msg.payload[1] == "O":
            if(state1 == True)or(state2 == True)or(state3 == True):
                client.publish("sven/home/Light1","OFF")
                client.publish("sven/home/Light2","OFF")
                client.publish("sven/home/Light3","OFF")
                state1 = False;
                state2 = False;
                state3 = False;
            else:
                client.publish("sven/home/Light1","ON")
                client.publish("sven/home/Light2","ON")
                client.publish("sven/home/Light3","ON")
                state1 = True;
                state2 = True;
                state3 = True;
    elif msg.topic == "sven/home/Lights0":
        if msg.payload[1] == "N":
            client.publish("sven/home/Light1","ON")
            client.publish("sven/home/Light2","ON")
            client.publish("sven/home/Light3","ON")
            client.publish("sven/home/Light4","ON")
            client.publish("sven/home/Light5","ON")
            client.publish("sven/home/Light6","ON")
            client.publish("sven/home/Light7","ON")
            client.publish("sven/home/Light8","ON")
            client.publish("sven/home/Light9","ON")
            client.publish("sven/home/Light10","ON")
            client.publish("sven/home/Light11","ON")
            client.publish("sven/home/Light12","ON")
            client.publish("sven/home/Light13","ON")
            client.publish("shellies/Light14/light/0/command","on")
            client.publish("shellies/Light15/light/0/command","on")
            client.publish("shellies/Light16/light/0/command","on")
            client.publish("shellies/Light17/light/0/command","on")
            client.publish("shellies/Light18/light/0/command","on")
            client.publish("shellies/Light19/light/0/command","on")
            client.publish("shellies/Light20/light/0/command","on")
            client.publish("shellies/Light21/light/0/command","on")
            client.publish("shellies/Light22/light/0/command","on")
            client.publish("shellies/Light23/light/0/command","on")
            client.publish("shellies/Light24/light/0/command","on")
            client.publish("shellies/Light25/color/0/command","on")
            client.publish("shellies/Light26/color/0/command","on")
            state1 = True;
            state2 = True;
            state3 = True;
            state4 = True;
            state5 = True;
            state3 = True;
            state6 = True;
            state7 = True;
            state8 = True;
            state9 = True;
            state10 = True;
            state11 = True;
            state12 = True;
            state13 = True;
            state14 = True;
            state15 = True;
            state16 = True;
            state17 = True;
            state18 = True;
            state19 = True;
            state20 = True;
            state21 = True;
            state22 = True;
            state23 = True;
            state24 = True;
            state25 = True;
            state26 = True;
        if msg.payload[1] == "F":
            client.publish("sven/home/Light1","OFF")
            client.publish("sven/home/Light2","OFF")
            client.publish("sven/home/Light3","OFF")
            client.publish("sven/home/Light4","OFF")
            client.publish("sven/home/Light5","OFF")
            client.publish("sven/home/Light6","OFF")
            client.publish("sven/home/Light7","OFF")
            client.publish("sven/home/Light8","OFF")
            client.publish("sven/home/Light9","OFF")
            client.publish("sven/home/Light10","OFF")
            client.publish("sven/home/Light11","OFF")
            client.publish("sven/home/Light12","OFF")
            client.publish("sven/home/Light13","OFF")
            client.publish("shellies/Light14/light/0/command","off")
            client.publish("shellies/Light15/light/0/command","off")
            client.publish("shellies/Light16/light/0/command","off")
            client.publish("shellies/Light17/light/0/command","off")
            client.publish("shellies/Light18/light/0/command","off")
            client.publish("shellies/Light19/light/0/command","off")
            client.publish("shellies/Light20/light/0/command","off")
            client.publish("shellies/Light21/light/0/command","off")
            client.publish("shellies/Light22/light/0/command","off")
            client.publish("shellies/Light23/light/0/command","off")
            client.publish("shellies/Light24/light/0/command","off")
            client.publish("shellies/Light25/color/0/command","off")
            client.publish("shellies/Light26/color/0/command","off")
            state1 = False;
            state2 = False;
            state3 = False;
            state4 = False;
            state5 = False;
            state3 = False;
            state6 = False;
            state7 = False;
            state8 = False;
            state9 = False;
            state10 = False;
            state11 = False;
            state12 = False;
            state13 = False;
            state14 = False;
            state15 = False;
            state16 = False;
            state17 = False;
            state18 = False;
            state19 = False;
            state20 = False;
            state21 = False;
            state22 = False;
            state23 = False;
            state24 = False;
            state25 = False;
            state26 = False;
        elif msg.payload[1] == "O":
            if(state6 == True)or(state7 == True)or(state8 == True):
                client.publish("sven/home/Light6","OFF")
                client.publish("sven/home/Light7","OFF")
                client.publish("sven/home/Light8","OFF")
                state6 = False;
                state7 = False;
                state8 = False;
            else:
                client.publish("sven/home/Light6","ON")
                client.publish("sven/home/Light7","ON")
                client.publish("sven/home/Light8","ON")
                state6 = True;
                state7 = True;
                state8 = True;
    elif msg.topic == "sven/home/Lights1":
        if msg.payload[1] == "N":
            client.publish("sven/home/Light6","ON")
            client.publish("sven/home/Light7","ON")
            client.publish("sven/home/Light8","ON")
            state6 = True;
            state7 = True;
            state8 = True;
        if msg.payload[1] == "F":
            client.publish("sven/home/Light6","OFF")
            client.publish("sven/home/Light7","OFF")
            client.publish("sven/home/Light8","OFF")
            state6 = False;
            state7 = False;
            state8 = False;
        elif msg.payload[1] == "O":
            if(state6 == True)or(state7 == True)or(state8 == True):
                client.publish("sven/home/Light6","OFF")
                client.publish("sven/home/Light7","OFF")
                client.publish("sven/home/Light8","OFF")
                state6 = False;
                state7 = False;
                state8 = False;
            else:
                client.publish("sven/home/Light6","ON")
                client.publish("sven/home/Light7","ON")
                client.publish("sven/home/Light8","ON")
                state6 = True;
                state7 = True;
                state8 = True;
    elif msg.topic == "sven/home/Lights2":
        if msg.payload[1] == "N":
            client.publish("sven/home/Light4","ON")
            client.publish("sven/home/Light5","ON")
            state4 = True;
            state5 = True;
        if msg.payload[1] == "F":
            client.publish("sven/home/Light4","OFF")
            client.publish("sven/home/Light5","OFF")
            state4 = False;
            state5 = False;
        elif msg.payload[1] == "O":
            if(state4 == True)or(state5 == True):
                client.publish("sven/home/Light4","OFF")
                client.publish("sven/home/Light5","OFF")
                state4 = False;
                state5 = False;
            else:
                client.publish("sven/home/Light4","ON")
                client.publish("sven/home/Light5","ON")
                state4 = True;
                state5 = True;
    elif msg.topic == "sven/home/Lights3":
        if msg.payload[1] == "N":
            client.publish("sven/home/Light9","ON")
            client.publish("sven/home/Light10","ON")
            state9 = True;
            state10 = True;
        if msg.payload[1] == "F":
            client.publish("sven/home/Light9","OFF")
            client.publish("sven/home/Light10","OFF")
            state9 = False;
            state10 = False;
        elif msg.payload[1] == "O":
            if(state9 == True)or(state10 == True):
                client.publish("sven/home/Light9","OFF")
                client.publish("sven/home/Light10","OFF")
                state9 = False;
                state10 = False;
            else:
                client.publish("sven/home/Light9","ON")
                client.publish("sven/home/Light10","ON")
                state9 = True;
                state10 = True;
    elif msg.topic == "sven/home/Lights4":
        if msg.payload[1] == "N":
            client.publish("sven/home/Light11","ON")
            client.publish("sven/home/Light12","ON")
            state11 = True;
            state12 = True;
        if msg.payload[1] == "F":
            client.publish("sven/home/Light11","OFF")
            client.publish("sven/home/Light12","OFF")
            state11 = False;
            state12 = False;
        elif msg.payload[1] == "O":
            if(state11 == True)or(state12 == True):
                client.publish("sven/home/Light11","OFF")
                client.publish("sven/home/Light12","OFF")
                state11 = False;
                state12 = False;
            else:
                client.publish("sven/home/Light11","ON")
                client.publish("sven/home/Light12","ON")
                state11 = True;
                state12 = True;
    elif msg.topic == "sven/home/Lights6":
        if msg.payload[1] == "N":
            client.publish("shellies/Light14/light/0/command","on")
            client.publish("shellies/Light15/light/0/command","on")
            client.publish("shellies/Light16/light/0/command","on")
            client.publish("shellies/Light17/light/0/command","on")
            client.publish("shellies/Light18/light/0/command","on")
            state14 = True;
            state15 = True;
            state16 = True;
            state17 = True;
            state18 = True;
        if msg.payload[1] == "F":
            client.publish("shellies/Light14/light/0/command","off")
            client.publish("shellies/Light15/light/0/command","off")
            client.publish("shellies/Light16/light/0/command","off")
            client.publish("shellies/Light17/light/0/command","off")
            client.publish("shellies/Light18/light/0/command","off")
            state14 = False;
            state15 = False;
            state16 = False;
            state17 = False;
            state18 = False;
        elif msg.payload[1] == "O":
            if(state14 == True)or(state15 == True)or(state16 == True)or(state17 == True)or(state18 == True):
                client.publish("shellies/Light14/light/0/command","off")#Shelly 14
                client.publish("shellies/Light15/light/0/command","off")
                client.publish("shellies/Light16/light/0/command","off")
                client.publish("shellies/Light17/light/0/command","off")
                client.publish("shellies/Light18/light/0/command","off")
                state14 = False;
                state15 = False;
                state16 = False;
                state17 = False;
                state18 = False;
            else:
                client.publish("shellies/Light14/light/0/command","on")
                client.publish("shellies/Light15/light/0/command","on")
                client.publish("shellies/Light16/light/0/command","on")
                client.publish("shellies/Light17/light/0/command","on")
                client.publish("shellies/Light18/light/0/command","on")
                state14 = True;
                state15 = True;
                state16 = True;
                state17 = True;
                state18 = True;
    elif msg.topic == "sven/home/Lights7":
        if msg.payload[1] == "N":
            client.publish("shellies/Light19/light/0/command","on")
            client.publish("shellies/Light20/light/0/command","on")
            client.publish("shellies/Light21/light/0/command","on")
            client.publish("shellies/Light19/light/0/set",'{"ison":true,"brightness":100}')
            client.publish("shellies/Light20/light/0/set",'{"ison":true,"brightness":100}')
            client.publish("shellies/Light21/light/0/set",'{"ison":true,"brightness":100}')
            state19 = True;
            state20 = True;
            state21 = True;
        if msg.payload[1] == "F":
            client.publish("shellies/Light19/light/0/command","off")
            client.publish("shellies/Light20/light/0/command","off")
            client.publish("shellies/Light21/light/0/command","off")
            state19 = False;
            state20 = False;
            state21 = False;
        elif msg.payload[1] == "O":
            if(state19 == True)or(state20 == True)or(state21 == True):
                client.publish("shellies/Light19/light/0/command","off")#Shelly 14
                client.publish("shellies/Light20/light/0/command","off")
                client.publish("shellies/Light21/light/0/command","off")
                state19 = False;
                state20 = False;
                state21 = False;
            else:
           	client.publish("shellies/Light19/light/0/command","on")
           	client.publish("shellies/Light20/light/0/command","on")
           	client.publish("shellies/Light21/light/0/command","on")
                client.publish("shellies/Light19/light/0/set",'{"ison":true,"brightness":100}')
                client.publish("shellies/Light20/light/0/set",'{"ison":true,"brightness":100}')
                client.publish("shellies/Light21/light/0/set",'{"ison":true,"brightness":100}')
                state19 = True;
                state20 = True;
                state21 = True;
    elif msg.topic == "sven/home/Lights8":
        if msg.payload[1] == "N":
            client.publish("shellies/Light22/light/0/command","on")
            client.publish("shellies/Light23/light/0/command","on")
            client.publish("shellies/Light24/light/0/command","on")
            state22 = True;
            state23 = True;
            state24 = True;
        if msg.payload[1] == "F":
            client.publish("shellies/Light22/light/0/command","off")
            client.publish("shellies/Light23/light/0/command","off")
            client.publish("shellies/Light24/light/0/command","off")
            state22 = False;
            state23 = False;
            state24 = False;
        elif msg.payload[1] == "O":
            if(state22 == True)or(state23 == True)or(state24 == True):
                client.publish("shellies/Light22/light/0/command","off")#Shelly 14
                client.publish("shellies/Light23/light/0/command","off")
                client.publish("shellies/Light24/light/0/command","off")
                state22 = False;
                state23 = False;
                state24 = False;
            else:
                client.publish("shellies/Light22/light/0/command","on")
                client.publish("shellies/Light23/light/0/command","on")
                client.publish("shellies/Light24/light/0/command","on")
                state22 = True;
                state23 = True;
                state24 = True;
    elif msg.topic == "sven/home/Light6/Status":
        if msg.payload[1] == "N":
            state6 = True;
        elif msg.payload[1] == "F":
            state6 = False;
    elif msg.topic == "sven/home/Light7/Status":
        if msg.payload[1] == "N":
            state7 = True;
        elif msg.payload[1] == "F":
            state7 = False;
    elif msg.topic == "sven/home/Light8/Status":
        if msg.payload[1] == "N":
            state7 = True;
        elif msg.payload[1] == "F":
            state7 = False;
    elif msg.topic == "sven/home/Light4/Status":
        if msg.payload[1] == "N":
            state4 = True;
        elif msg.payload[1] == "F":
            state4 = False;
    elif msg.topic == "sven/home/Light5/Status":
        if msg.payload[1] == "N":
            state5 = True;
        elif msg.payload[1] == "F":
            state5 = False;
    elif msg.topic == "sven/home/Light1/Status":
        if msg.payload[1] == "N":
            state1 = True;
        elif msg.payload[1] == "F":
            state1 = False;
    elif msg.topic == "sven/home/Light2/Status":
        if msg.payload[1] == "N":
            state2 = True;
        elif msg.payload[1] == "F":
            state2 = False;
    elif msg.topic == "sven/home/Light3/Status":
        if msg.payload[1] == "N":
            state3 = True;
        elif msg.payload[1] == "F":
            state3 = False;
    elif msg.topic == "sven/home/Light9/Status":
        if msg.payload[1] == "N":
            state9 = True;
        elif msg.payload[1] == "F":
            state9 = False;
    elif msg.topic == "sven/home/Light10/Status":
        if msg.payload[1] == "N":
            state10 = True;
        elif msg.payload[1] == "F":
            state10 = False;
    elif msg.topic == "sven/home/Light11/Status":
        if msg.payload[1] == "N":
            state11 = True;
        elif msg.payload[1] == "F":
            state11 = False;
    elif msg.topic == "sven/home/Light12/Status":
        if msg.payload[1] == "N":
            state12 = True;
        elif msg.payload[1] == "F":
            state12 = False;
    elif msg.topic == "sven/home/Light13/Status":
        if msg.payload[1] == "N":
            state13 = True;
        elif msg.payload[1] == "F":
            state13 = False;
    elif msg.topic == "sven/home/Light14":
        if msg.payload[1] == "N":
            state14 = True
            client.publish("shellies/Light14/light/0/command","on")
        elif msg.payload[1] == "F":
            state14 = False
            client.publish("shellies/Light14/light/0/command","off")
        elif msg.payload[1] == "O":
            if(state14 == True):
                client.publish("shellies/Light14/light/0/command","off")
                state14 = False
            else:
                client.publish("shellies/Light14/light/0/command","on")
                state14 = True
    elif msg.topic == "sven/home/Light15":
        if msg.payload[1] == "N":
            state15 = True
            client.publish("shellies/Light15/light/0/command","on")
        elif msg.payload[1] == "F":
            state15 = False
            client.publish("shellies/Light15/light/0/command","off")
        elif msg.payload[1] == "O":
            if(state14 == True):
                client.publish("shellies/Light15/light/0/command","off")
                state15 = False
            else:
                client.publish("shellies/Light15/light/0/command","on")
                state15 = True
    elif msg.topic == "sven/home/Light16":
        if msg.payload[1] == "N":
            state16 = True
            client.publish("shellies/Light16/light/0/command","on")
        elif msg.payload[1] == "F":
            state16 = False
            client.publish("shellies/Light16/light/0/command","off")
        elif msg.payload[1] == "O":
            if(state14 == True):
                client.publish("shellies/Light16/light/0/command","off")
                state16 = False
            else:
                client.publish("shellies/Light16/light/0/command","on")
                state16 = True
    elif msg.topic == "sven/home/Light17":
        if msg.payload[1] == "N":
            state17 = True
            client.publish("shellies/Light17/light/0/command","on")
        elif msg.payload[1] == "F":
            state17 = False
            client.publish("shellies/Light17/light/0/command","off")
        elif msg.payload[1] == "O":
            if(state17 == True):
                client.publish("shellies/Light17/light/0/command","off")
                state17 = False
            else:
                client.publish("shellies/Light17/light/0/command","on")
                state17 = True
    elif msg.topic == "sven/home/Light18":
        if msg.payload[1] == "N":
            state18 = True
            client.publish("shellies/Light18/light/0/command","on")
        elif msg.payload[1] == "F":
            state18 = False
            client.publish("shellies/Light18/light/0/command","off")
        elif msg.payload[1] == "O":
            if(state14 == True):
                client.publish("shellies/Light18/light/0/command","off")
                state18 = False
            else:
                client.publish("shellies/Light18/light/0/command","on")
                state18 = True
    elif msg.topic == "sven/home/Light19":
        if msg.payload[1] == "N":
            state19 = True
            client.publish("shellies/Light19/light/0/command","on")
        elif msg.payload[1] == "F":
            state19 = False
            client.publish("shellies/Light19/light/0/command","off")
        elif msg.payload[1] == "O":
            if(state19 == True):
                client.publish("shellies/Light19/light/0/command","off")
                state19 = False
            else:
                client.publish("shellies/Light19/light/0/command","on")
                state19 = True
    elif msg.topic == "sven/home/Light20":
        if msg.payload[1] == "N":
            state20 = True
            client.publish("shellies/Light20/light/0/command","on")
        elif msg.payload[1] == "F":
            state20 = False
            client.publish("shellies/Light20/light/0/command","off")
        elif msg.payload[1] == "O":
            if(state20 == True):
                client.publish("shellies/Light20/light/0/command","off")
                state20 = False
            else:
                client.publish("shellies/Light20/light/0/command","on")
                state20 = True
    elif msg.topic == "sven/home/Light21":
        if msg.payload[1] == "N":
            state21 = True
            client.publish("shellies/Light21/light/0/command","on")
        elif msg.payload[1] == "F":
            state21 = False
            client.publish("shellies/Light21/light/0/command","off")
        elif msg.payload[1] == "O":
            if(state21 == True):
                client.publish("shellies/Light21/light/0/command","off")
                state21 = False
            else:
                client.publish("shellies/Light21/light/0/command","on")
                state21 = True
    elif msg.topic == "sven/home/Light22":
        if msg.payload[1] == "N":
            state22 = True
            client.publish("shellies/Light22/light/0/command","on")
        elif msg.payload[1] == "F":
            state22 = False
            client.publish("shellies/Light22/light/0/command","off")
        elif msg.payload[1] == "O":
            if(state22 == True):
                client.publish("shellies/Light22/light/0/command","off")
                state22 = False
            else:
                client.publish("shellies/Light22/light/0/command","on")
                state22 = True
    elif msg.topic == "sven/home/Light23":
        if msg.payload[1] == "N":
            state23 = True
            client.publish("shellies/Light23/light/0/command","on")
        elif msg.payload[1] == "F":
            state23 = False
            client.publish("shellies/Light23/light/0/command","off")
        elif msg.payload[1] == "O":
            if(state23 == True):
                client.publish("shellies/Light23/light/0/command","off")
                state23 = False
            else:
                client.publish("shellies/Light23/light/0/command","on")
                state23 = True
    elif msg.topic == "sven/home/Light24":
        if msg.payload[1] == "N":
            state24 = True
            client.publish("shellies/Light24/light/0/command","on")
        elif msg.payload[1] == "F":
            state24 = False
            client.publish("shellies/Light24/light/0/command","off")
        elif msg.payload[1] == "O":
            if(state24 == True):
                client.publish("shellies/Light24/light/0/command","off")
                state24 = False
            else:
                client.publish("shellies/Light24/light/0/command","on")
                state24 = True
    elif msg.topic == "sven/home/Light25":
        if msg.payload[1] == "N":
            state25 = True
            client.publish("shellies/Light25/color/0/command","on")
        elif msg.payload[1] == "F":
            state25 = False
            client.publish("shellies/Light25/color/0/command","off")
        elif msg.payload[1] == "O":
            if(state25 == True):
                client.publish("shellies/Light25/color/0/command","off")
                state25 = False
            else:
                client.publish("shellies/Light25/color/0/command","on")
                state25 = True
    elif msg.topic == "sven/home/Light26":
        if msg.payload[1] == "N":
            state26 = True
            client.publish("shellies/Light26/color/0/command","on")
        elif msg.payload[1] == "F":
            state26 = False
            client.publish("shellies/Light26/color/0/command","off")
        elif msg.payload[1] == "O":
            if(state26 == True):
                client.publish("shellies/Light26/color/0/command","off")
                state26 = False
            else:
                client.publish("shellies/Light26/color/0/command","on")
                state26 = True
    #send_status()
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

