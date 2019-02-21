# WindSensor-and-Nagios
This project takes input from a wind sensor and sends the information to a Nagios XI server to be monitored.

Flow if information: Wind Sensor > Arduino > Serial Monitor > Raspberry Pi 3 B > Python3.5.3 > Nagios XI

Nagios XI sends an active check to the raspberry Pi via NRPE which runs the script check_MPH.py. The python script reads the serial port that is constantly recieving data from the arduino. The script prints out information that is sent back to the Nagios XI server and recorded. 
