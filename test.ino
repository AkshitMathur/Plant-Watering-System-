int water; // Declare water variable to store the water level reading

void setup() {
  pinMode(3, OUTPUT); // Set pin 3 as an output for relay board, to send signal to the relay
  pinMode(6, INPUT); // Set pin 6 as an input for receiving signal from soil sensor
}

void loop() { 
  water = digitalRead(6);  // Read the signal from the soil sensor and store it in the water variable
  if (water == HIGH) // If water level is full, then cut off the relay 
  {
    digitalWrite(3, LOW); // Set pin 3 to LOW to cut off the relay
  }
  else // If water level is not full
  {
    digitalWrite(3, HIGH); // Set pin 3 to HIGH to continue providing signal and water supply
  }
  delay(400); // Delay for 400 milliseconds to provide stability
}
