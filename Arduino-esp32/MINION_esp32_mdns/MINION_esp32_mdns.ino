#include <WiFi.h>
#include <ESPmDNS.h>

const char* ssid = "UniOfCam-IoT";
const char* password = "AiT4Qt59";



void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi network
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");

  // Set up mDNS
  if (!MDNS.begin("esp32_minion_n1")) {
    Serial.println("Error setting up mDNS");
  } else {
    Serial.println("mDNS responder started");
  }

//  // Advertise IP address over mDNS
//  MDNS.addService("http", "tcp", 80);

  // Advertise device information over mDNS
  MDNS.addService("http", "tcp", 20000);
  MDNS.addServiceTxt("http", "tcp", "device_type", "ESP32");
  MDNS.addServiceTxt("http", "tcp", "mac_address", WiFi.macAddress());
  MDNS.addServiceTxt("http", "tcp", "owner", "Anand");
}

void loop() {
  // Nothing to do here
}
