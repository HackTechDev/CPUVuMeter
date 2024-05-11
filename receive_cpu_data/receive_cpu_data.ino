const int ledPin3 = 3;
const int ledPin4 = 4;
const int ledPin5 = 5;
const int ledPin9 = 9;
const int ledPin10 = 10;
const int ledPin11 = 11;



void setup() {
  Serial.begin(9600);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);
  pinMode(ledPin5, OUTPUT);
  pinMode(ledPin9, OUTPUT);
  pinMode(ledPin10, OUTPUT);
  pinMode(ledPin11, OUTPUT);
}

void loop() {
  // Read the incoming data
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int pin = data.substring(0, data.indexOf(':')).toInt();
    int value = data.substring(data.indexOf(':') + 1).toInt();
    
    // Set the PWM value
    analogWrite(pin, value);
  }
}
