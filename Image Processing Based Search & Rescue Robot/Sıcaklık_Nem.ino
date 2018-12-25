#include <dht.h>

dht DHT;
void setup() {
 Serial.begin(9600);
 
}
void loop() {
 int readData = DHT.read22(A0);
 float t = DHT.temperature;
 float h = DHT.humidity;
 
 Serial.println(t); 
 Serial.println(h); 
 Serial.println("-------------------"); 
 delay(2000);
}
