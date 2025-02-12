#include <Blynk.h>

#include <Servo.h>

// Define pins for ultrasonic sensor
const int trigPin = 9;
const int echoPin = 10;

// Define two servo motors
Servo servo1; // Servo for "organic"
Servo servo2; // Servo for "recyclable"
const int servoPin1 = 3; // Pin for Servo 1 (organic)
const int servoPin2 = 5; // Pin for Servo 2 (recyclable)

// Variables
long duration;
int distance;
int piResponse;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Set up ultrasonic sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Attach servo motors
  servo1.attach(servoPin1);
  servo2.attach(servoPin2);

  // Move both servos to neutral position
  servo1.write(0);
  servo2.write(0);
}

void moveServo(Servo &servo) {
  // Move from 0 to 180 degrees
  for (int pos = 0; pos <= 180; pos++) {
    servo.write(pos); // Set the servo position
    delay(15);        // Wait 15ms for the servo to reach the position
  }

  delay(1000); // Pause for 1 second at 180 degrees

  // Move back from 180 to 0 degrees
  for (int pos = 180; pos >= 0; pos--) {
    servo.write(pos); // Set the servo position
    delay(15);        // Wait 15ms for the servo to reach the position
  }

  delay(1000); // Pause for 1 second at 0 degrees
}

void loop() {
  // Measure distance using ultrasonic sensor
  distance = getDistance();

  // If object is detected within 10 cm, send data to Raspberry Pi
  if (distance > 0 && distance <= 10) {
    Serial.println(1); // Send "1" to Raspberry Pi
  } else {
    Serial.println(0); // Send "0" to Raspberry Pi
  }

  // Wait for Raspberry Pi response
  if (Serial.available() > 0) {
    piResponse = Serial.parseInt(); // Read response from Raspberry Pi

    if (piResponse == 0) {
      moveServo(servo2); // Move the second servo (recyclable)
    } else if (piResponse == 1) {
      moveServo(servo1); // Move the first servo (organic)
    }
  }

  delay(100); // Short delay for stability
}

int getDistance() {
  // Send a 10us pulse to trigger pin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Read the echo pin and calculate the distance
  duration = pulseIn(echoPin, HIGH);
  int distance = duration * 0.034 / 2; // Convert to cm

  return distance;
}
