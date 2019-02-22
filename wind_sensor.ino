/*
Created By: Daniel Cronk
Created On: 2/15/2019
Last Modified: 2/15/2019
Created For: Honda of America Mfg.

Use this program to print wind speed to serial monitor.

*/

const int windPin = A0;
const int tempPin = A2;

void setup(){
  Serial.begin(9600);
}

void loop(){
  
  int windADunits = analogRead(windPin);
  float windMPH = pow((((float)windADunits - 264.0) / 85.6814), 3.36814);
  Serial.print(windMPH);
  Serial.print('\n');
  
  delay(1000);
}
