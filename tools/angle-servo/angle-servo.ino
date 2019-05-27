/*
Utilitaire pour positionner l'angle d'un servo.

*/
#include <Servo.h>

Servo myservo;
#define SERVO_PIN 5;

int angle = 0;    //angle initial

void setup() {
  Serial.begin(9600);
  myservo.attach(SERVO_PIN);
}

void positionner(int angle) {
  Serial.print("Position demandee : ");
  Serial.println(angle);
  myservo.write(pos);
  //delay(1000);
}


void loop() {
  if (Serial.available() > 0) {
    Serial.println("angle: ");
    angle = Serial.parseInt();
    positionner(angle);  
  }
  
}
