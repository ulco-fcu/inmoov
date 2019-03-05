/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  Serial.begin(9600);
  myservo.attach(3);  // attaches the servo on pin 9 to the servo object
}

void positionner(int pos) {
  Serial.print("Position demandee : ");
  Serial.println(pos);
  //pos = map(pos, 0,90,24,113);
  //pos = map(pos, 0,90,24,124);
  //33->121
  //pos = map(pos, 0,90,33,121);
  //34-149 : min max du servo : mais depasse les 90 deg (rotation de 115°) 
  // pour reduire a 90 on a 115-90 = 25 de marge, soit 12 de chaque coté [0-90]->[34+12 - 149-12] -> [46 - 137]
  //pos = map(pos,0,90,46,137);
  // ou si on conserve le 0 à 34 : [0-90] -> [34+0 - 149-24] -> [34 - 125]
  //pos = map(pos,0,90,34,125);
  //ou si on conserve l'origine : [0-115] -> [34-149]
  pos = map(pos, 0,115,34,149);
  Serial.print("Position mappée : ");
  Serial.println(pos);
  
  myservo.write(pos);
  //delay(1000);
}

void loop() {
  
  if (Serial.available() > 0) {
    Serial.println("angle: ");
    pos = Serial.parseInt();
    positionner(pos);  
  }
  
}
