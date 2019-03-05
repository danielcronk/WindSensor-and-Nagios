# WindSensor-and-Nagios
This project takes input from a wind sensor and sends the information to a Nagios XI server to be monitored.
Flow of information: Wind Sensor > Arduino > Serial Monitor > Raspberry Pi 3 B > Python3.5.3 > Nagios XI. 
Nagios XI sends an active check to the Raspberry Pi via NRPE which runs the script check_MPH.py. The python script reads the serial port that is constantly recieving data from the arduino. The script prints out information that is sent back to the Nagios XI server and recorded. 

One of the main resaons for posting this project is to help others in creating basic custom NRPE plugins via Python. It took me quite a bit of time and research to figure this out, so I am going to condense it all to one place to hopefully help someone out.
