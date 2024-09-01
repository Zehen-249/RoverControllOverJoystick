#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoJson.h> // Include the ArduinoJson library
#include "controll.h"

const char *ssid = "POCO M4 Pro";
const char *password = "PocoPro4";
int newSpeed = 0;

WiFiUDP udp;
unsigned int localUdpPort = 12345; // Same port as in the Python script
char incomingPacket[255];          // Buffer for incoming packets

String dataToDisplay = "No data received yet";

Rover rover = {
    .left_f_pwm = 32,
    .left_f_DIR = 33,
    .right_f_pwm = 25,
    .right_f_DIR = 26,
    .left_b_pwm = 27,
    .left_b_DIR = 14,
    .right_b_pwm = 12,
    .right_b_DIR = 13,
    .speed = 0
  };

void setup()
{
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
  udp.begin(localUdpPort);
  Serial.printf("UDP server started at port %d\n", localUdpPort);
  make_setup(&rover);
}

void loop()
{
  run(&rover);
  // Check for incoming UDP packets
  int packetSize = udp.parsePacket();
  if (packetSize)
  {
    int len = udp.read(incomingPacket, 255);
    if (len > 0)
    {
      incomingPacket[len] = 0;
    }

    // Serial.printf("Received packet: %s\n", incomingPacket);

    // Parse the incoming JSON data
    DynamicJsonDocument doc(1024);
    DeserializationError error = deserializeJson(doc, incomingPacket);

    if (!error)
    {
      String DIR = doc["type"];
      int newSpeed = doc["value"];

      // Format the data for display
      String dataToDisplay = "Type: " + String(DIR) + " Value: " + String(newSpeed);
      set_dir(DIR, &rover);

      if (newSpeed != rover.speed)
      {
        if (newSpeed > rover.speed && (newSpeed - rover.speed > 5))
        {
          while (rover.speed < newSpeed)
          {
            rover.speed++;
            set_speed(&rover, rover.speed);
            run(&rover);
          }
        }
        else if (newSpeed < rover.speed && (rover.speed - newSpeed > 5))
        {
          while (rover.speed > newSpeed)
          {
            rover.speed--;
            set_speed(&rover, rover.speed);
            run(&rover);
          }
        }
      }
      // Serial.printf("DIR %s Speed %d\n",DIR,rover.speed);
      
    }
    else
    {
      Serial.println("Failed to parse JSON");
    }
  }
}
