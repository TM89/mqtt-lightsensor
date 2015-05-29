#include "pitches.h"

int potentiometerPin = A0;
int photoresistorPin = A1;
int ledPin = 13;      // select the pin for the LED
int potentiometerValue = 0;  // variable to store the value coming from the sensor
int photoresistorValue = 0;
int noteDuration = 250;

void setup() {
  // declare the ledPin as an OUTPUT:
  pinMode(ledPin, OUTPUT);  
  Serial.begin(9600);
}

void loop() {
  // read the value from the sensor:
  potentiometerValue = analogRead(potentiometerPin);
  photoresistorValue = analogRead(photoresistorPin);  
  // turn the ledPin on
  digitalWrite(ledPin, HIGH);         
  // turn the ledPin off:
  delay(potentiometerValue);
  digitalWrite(ledPin, LOW);  
  tone(8, photoresistorValue,noteDuration);

    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);
    // stop the tone playing:
    noTone(8);  
  digitalWrite(ledPin, LOW);
  Serial.println(photoresistorValue);//+"_"+photoresistorValue);  
  // stop the program for for <sensorValue> milliseconds:
  delay(20);                  
}
