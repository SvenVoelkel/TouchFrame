/*
 * Das hier ist der Code, der auf allen Sonoffs läuft. 

*/

/*
    This Code is running on all the Sonoffs. 
*/

#include <ESP8266WiFi.h>
#include <PubSubClient.h>

//Wifi-Credentials. 
const char* ssid = "Network 6098ab";
const char* password = "abcdefgh";
const char* mqtt_server = "10.0.1.2";


WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;

//Relais Pin is the GPIO that has to be switched to switch the High-Voltage Relais of the Sonoff.
int relaisPin=12;
//Button Pin is the onboard Button.
int buttonPin=0;
//LedPin is the Onboard-LED. 
int ledPin=13;

bool state=false;

void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is acive low on the ESP-01)
  } else {
    digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off by making the voltage HIGH
  }

  if (payload[1]=='C')
  {
    client.publish("sven/home/Light14/Alive", "TRUE");
  }
  else if ((char)payload[1] == 'F') 
  {
    Serial.print("Turning Off");
    digitalWrite(relaisPin, LOW);
    client.publish("sven/home/Light14/Status", "OFF");
    state=false;
  } else if (payload[1]=='N')
  {
    Serial.print("Turning On");
    digitalWrite(relaisPin, HIGH);
    client.publish("sven/home/Light14/Status", "ON");
    state=true;
  } else if(payload[1]=='O') 
  {
    if(state)
    {
      Serial.print("Turning Off");
      digitalWrite(relaisPin, LOW);
      client.publish("sven/home/Light14/Status", "OFF");
      state=false;
    }
    else
    {
      Serial.print("Turning On");
      digitalWrite(relaisPin, HIGH);
      client.publish("sven/home/Light14/Status", "ON");
      state=true;
    }
  
  }
  if(state){
      digitalWrite(ledPin, LOW);
  }
  else
  {
      digitalWrite(ledPin, HIGH);
  }

}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe("sven/home/Light14");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  client.subscribe("sven/home/Light14");
  client.publish("sven/home/Light14/Status", "ON");
  
  pinMode(relaisPin, OUTPUT);
  pinMode(buttonPin, INPUT);
  
  digitalWrite(relaisPin, HIGH);
  
}

void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  if(!digitalRead(buttonPin))
  {
    if(state)
    {
      Serial.print("Turning Off");
      digitalWrite(relaisPin, LOW);
      client.publish("sven/home/Light14/Status", "OFF");
      state=false;
      digitalWrite(ledPin, HIGH);
    }
    else
    {
      Serial.print("Turning On");
      digitalWrite(relaisPin, HIGH);
      client.publish("sven/home/Light14/Status", "ON");
      state=true;
      digitalWrite(ledPin, LOW);
    }
    while(!digitalRead(buttonPin))
    {
      delay(10);
    }
  }
}
