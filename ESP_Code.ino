/*
   Dieses Programm nutzt keinen Schlafmodus und hat daher einen hohen Energieverbrauch. 
   Dauerhafte Verbindung zum Wifi-Netzwerk. 
   Das Licht geht bei Berührung an und
   wenn der Auftrag durch ist wieder aus.
   Version, die mit dem AT42QT1070 arbeiten soll.
   Version ohne Batteriebetrieb!
   Nur für feste Stromversorgung zu empfehlen. 
*/
/*
    Current Version NOT using Light Sleep Mode. 
    Always connected to network.  
    LED turns on after touch and turned off after handling of the touch. 
    Version that is meant to be used with AT42QT1070.
    Version uses MQTT for communication.
    Recommended to be used with fixed power supply. 
*/

#include "Arduino.h"
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <Wire.h>
#include <PubSubClient.h>

#define FPM_SLEEP_MAX_TIME 0xFFFFFFF
// Required for LIGHT_SLEEP_T delay mode

extern "C" {
#include "user_interface.h"
}


#define LIGHT_WAKE_PIN 14

boolean touchStates[7]; //to keep track of the previous touch states

//Wifi-Credentials
const char* ssid = "Network 6098ab";
const char* password = "abcdefgh";

//#################################################################################
//Predefined ip Adress (10.0.1.XXX)
const int ipAddress = 120;

//The Topics that are called by triggering the main touch Pins of the QT1070 are entered here. 
//all necessary programming that is different between the different systems can be done in this upper part of the program. 
char* outputTopic1 = "sven/home/Lights1"; //Topic for Electrode 0
char* outputTopic2 = "sven/home/Light13"; //Topic for Electrode 2

//BSSID of the router is hardcoded here for faster connection.
  //This restricts this programm to be only used with exactly this router.
//uint8_t bssid[] = {0x68, 0xA8, 0x6D, 0x60, 0x98, 0xAB}; //Airport Express
uint8_t bssid[] = {0xBC, 0x05, 0x43, 0x13, 0x4F, 0xDC}; //FritzBox

WiFiClient espClient;
HTTPClient http;
PubSubClient client(espClient);


//The MQTT Server on the Raspberry Pi (10.0.1.2:1883)
const char* mqtt_server = "10.0.1.2";
long lastMsg = 0;
char msg[50];

boolean pinTouched[7] = {false, false, false, false, false, false,
                         false
                        };

//Variables to store timestamps. (For connection duration evaluation). (Not used in this battery-less scenario but still kept in code)
long startUp;
long connectedWifi;
long connectedHttp;


//TouchCounter is used to enforce a reboot if too many touches happen in too little time. this will be diagnosed as a malfunction.
long firstTouch;
int touchCounter = 0;

//The setup function is called once at startup of the sketch
void setup() {
  Serial.begin(115200);
  while (!Serial) { }
  Serial.println();
  Serial.println("Start device in normal mode!");
  pinMode(BUILTIN_LED, OUTPUT);

  pinMode(14, INPUT);
  digitalWrite(14, HIGH);
  pinMode(16, INPUT);
  digitalWrite(16, HIGH);

  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);


  qt1070_setup();
  Wire.begin();
  setup_wifi();
  if (!client.connected()) {
    reconnect();
  }
  char outputTopic[64];
  sprintf(outputTopic, "sven/home/Sensor/%d", ipAddress);
  //Serial.println(outputString);
  //strcat(outputString, );
  client.publish(outputTopic, "restarted");
  firstTouch = millis();
}

void callbacko() {
  Serial.println("Callback");
  Serial.flush();
}

void setup_wifi() {
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  int32_t channel = 6;
  IPAddress ip(10, 0, 1, ipAddress);
  IPAddress subnet(255, 255, 255, 0);
  IPAddress gateway(10, 0, 1, 1);
  IPAddress dns(8, 8, 8, 8);
  WiFi.config(ip, dns, gateway, subnet);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password, channel, bssid, true);

  while (WiFi.status() != WL_CONNECTED) {
    collectTouches();
    delay(100);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}


void callback(char* topic, byte* payload, unsigned int length) {
}

void loop() {
  digitalWrite(BUILTIN_LED, HIGH);
    
  //Light Sleep Mode is not being used in this scenario.
  /*
    Serial.println("Enter light sleep mode");

    gpio_pin_wakeup_enable(GPIO_ID_PIN(LIGHT_WAKE_PIN), GPIO_PIN_INTR_LOLEVEL);
    wifi_set_opmode(NULL_MODE);
    wifi_fpm_set_sleep_type(LIGHT_SLEEP_T);
    wifi_fpm_open();
    wifi_fpm_set_wakeup_cb(callbacko);
    wifi_fpm_do_sleep(FPM_SLEEP_MAX_TIME);
    delay(100);

    Serial.println("Exit light sleep mode");
  */

  startUp = millis();

  //The Microcontroller will periodically check whether a touch has happened. 
  for (int i = 0; i < 7; i++) {
    pinTouched[i] = false;
  }
  readTouchInputs();
  boolean stillTouched = false;
  for (int i = 0; i < 7; i++) {
    if (touchStates[i] == true) {
      stillTouched = true;
    }
  }

  //only if a touch has occured will the ESP connect to Wifi and check for other inputs
  if (stillTouched) {
    digitalWrite(BUILTIN_LED, LOW);
    connectedWifi = millis();
      
      
    //This bit of code is to detect a faulty Sensor (Babbling Idiot).
    //If there are more than five touches within five seconds, the ESP will reboot.
    touchCounter = touchCounter + 1;
    if (touchCounter >= 5)
    {
      if (millis() - firstTouch < 4000)
      {
        Serial.println("Overload, too sensitive // Overload, too sensitive // Overload, too sensitive // ");
        
        char outputTopic[64];
        sprintf(outputTopic, "sven/home/Sensor/%d", ipAddress);
        client.publish(outputTopic, "overload");   
        delay(1000);
        ESP.restart();
      }
      else
      {
        firstTouch = millis();
      }
      touchCounter=0;
    }

    handleTouches();

    //After the initital touches have been handled, the ESP sends out the statistics
    //containing the durations of the wifi connect and http connect.
    sendStatistics();

    //wait at least 1 second after the first touch for other inputs.

    while (stillTouched)
    {
      readTouchInputs();
      handleTouches();

      //The ESP will wait until all the touch Pins have been released.
      stillTouched = false;
      for (int i = 0; i < 7; i++) {
        if (touchStates[i] == true) {
          stillTouched = true;
        }
      }
      Serial.println(stillTouched);
      Serial.println("Wir sind hier");
      delay(100);
    }
    digitalWrite(BUILTIN_LED, HIGH);
  }

  //wifi_set_sleep_type(NONE_SLEEP_T);
  delay(50);
}

void handleTouches() {
  //Before calling this function, the ESP connected to Wifi and collected information on which
  //touch pins have been touched. This function then sends out an MQTT Message for every one
  //of those pins.
  if (pinTouched[0] == true || pinTouched[1] == true || pinTouched[2] == true ||
      pinTouched[3] == true || pinTouched[6] == true) {
    if (!client.connected()) {
      reconnect();
      connectedHttp = millis();
    }

    char outputPayload[64];
    sprintf(outputPayload, "TOGGLE %d", ipAddress);

    if (pinTouched[0] == true) {
      //#######################################################################################

      client.publish(outputTopic1, outputPayload);
      Serial.println(outputPayload);
    }
    if (pinTouched[1] == true) {


    }
    if (pinTouched[2] == true) {
      //#######################################################################################
      client.publish(outputTopic2, outputPayload);
      Serial.println(outputPayload);
    }
    if (pinTouched[3] == true) {
      char* outputPost = "topic=sven/home/Lights2&payload=TOGGLE";
      http.addHeader("Content-Type", "application/x-www-form-urlencoded");
      //int httpResponseCode = http.POST(outputPost);
      Serial.println(outputPost);
      //Serial.println(httpResponseCode);
    }
  }

  //after having sent out the MQTT Messages. The ESP deletes the information of newly touched Pins.
  for (int i = 0; i < 7; i++) {
    pinTouched[i] == false;
  }
  connectedHttp = millis();
}

void readTouchInputs() {
  //read the touch state from the QT1070
  //On the QT1070, the key values are stored in register 3.
  Wire.beginTransmission(0x1B); // transmit to device
  Wire.write(0x03); // want to read key status // set pointer
  Wire.endTransmission();      // stop transmitting
  Wire.requestFrom(0x1B, 1);    // request 1 byte from slave device
  int touched = Wire.read();
  int val = touched;
  for (int i = 7; 0 <= i; i--) {
    printf("%c", (val & (1 << i)) ? '1' : '0');
  }
  Serial.println();
  for (int i = 0; i < 7; i++) { // Check what electrodes were pressed
    pinTouched[i] = false;
    if (touched & (1 << i)) {
      if (touchStates[i] == 0) {
        Serial.print(i);
        Serial.println(" was just touched");
        pinTouched[i] = true;
        touchStates[i] = 1;
      }
    }
    else {
      if (touchStates[i] == 1) {
        Serial.print(i);
        Serial.println(" is no longer being touched");
      }
      touchStates[i] = 0;
    }
  }
}


void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    char uniqueName[64];
    sprintf(uniqueName, "ESP8266Client%d", ipAddress);
    if (client.connect(uniqueName)) {
      Serial.println("connected");
      // Once connected, publish an announcement...
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 0.5 seconds");
      // Wait 5 seconds before retrying
      delay(500);
    }
  }
}

//This function is used to send out the monitoring data of how long it took to connect to the network. 
void sendStatistics()
{
  long wifiTime = connectedWifi - startUp;
  long httpTime = connectedHttp - connectedWifi;
  Serial.print("WiFi: ");
  Serial.println(wifiTime);
  Serial.print("HTTP: ");
  Serial.println(httpTime);

  char outputPayload[32];
  sprintf(outputPayload, "WiFi: %ld, HTTP: %ld", wifiTime, httpTime);
  char outputPost[64];
  sprintf(outputPost, "topic=sven/home/Sensor/%d&payload=%s", ipAddress, outputPayload);
  Serial.println(outputPost);
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");
  //int httpResponseCode = http.POST(outputPost);

  char outputTopic[64];
  sprintf(outputTopic, "sven/home/Sensor/%d", ipAddress);
  //Serial.println(outputString);
  //strcat(outputString, );
  client.publish(outputTopic, outputPayload);

}

void collectTouches() {
  //read the touch state from the QT1070
  //On the QT1070, the key values are stored in register 3.
  Wire.beginTransmission(0x1B); // transmit to device
  Wire.write(0x03); // want to read key status // set pointer
  Wire.endTransmission();      // stop transmitting
  Wire.requestFrom(0x1B, 1);    // request 1 byte from slave device
  int touched = Wire.read();
  for (int i = 0; i < 7; i++) { // Check what electrodes were pressed
    if (touched & (1 << i)) {
      pinTouched[i] = true;
      touchStates[i] = true;
    }
  }
}

void qt1070_setup(void) {
  Serial.println("Setup the QT1070");
  //set_register(address, register, value);
  //set_register(0x1B, 0x01, 0x01);

  // Set Max On Duration
  // After a set maximum amount of time, the pin will be reset and recalibrated.
  // Adresses 55 (0x37)
  // Default 180 (160 ms × 180 = 28.8s)

  set_register(0x1B, 0x37, 0x00);

  // Set AVE (Averaging Factor / Turn the Key Off)
  // and AKS (Only one Key in a Group may be touched at the same time)
  // Adresses 39-45 (0x27 - 0x2D)
  // 6 Bits for AVE, 2 Bits for AKS
  // Default AVE = 8.  Default AKS is 1 but should be 0 here.

  set_register(0x1B, 0x27, 0x81); // Turn on  Key 0
  set_register(0x1B, 0x28, 0x00); // Turn off Key 1
  set_register(0x1B, 0x29, 0x82); // Turn on  Key 2
  set_register(0x1B, 0x2A, 0x00); // Turn off Key 3
  set_register(0x1B, 0x2B, 0x00); // Turn off Key 4
  set_register(0x1B, 0x2C, 0x00); // Turn off Key 5
  set_register(0x1B, 0x2D, 0x00); // Turn off Key 6


  // Set DI (Detection Integrator)
  // Adresses 46-52 (0x2E - 0x34)
  // Default DI = 4
  set_register(0x1B, 0x2E, 0x08); // Set DI Key 0
  set_register(0x1B, 0x30, 0x08); // Set DI Key 2

  //################################################################################################
  // Set Threshold-Values
  // Adresses 32-38 (0x20 - 0x26)
  // Default = 20 (0x14) 0 would be hypersensitive.

  set_register(0x1B, 0x20, 0x01); // Turn on  key 0
  set_register(0x1B, 0x22, 0x01); // Turn on  Key 2


  // Set Low Power Mode
  // Sets Time between two consecutive Measurements
  // Adresses 54 (0x36)
  // Default = 2 (0x02) 255 would be over 2 seconds.

  set_register(0x1B, 0x36, 0x08); // Turn on  key 0


}

boolean checkInterrupt(void) {
  digitalRead(14);
}

void set_register(int address, unsigned char r, unsigned char v) {
  Wire.beginTransmission(address);
  Wire.write(r);
  Wire.write(v);
  Wire.endTransmission();
}
