const int ledPin = 9;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
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
