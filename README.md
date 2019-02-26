# WindSensor-and-Nagios
This project takes input from a wind sensor and sends the information to a Nagios XI server to be monitored.
Flow of information: Wind Sensor > Arduino > Serial Monitor > Raspberry Pi 3 B > Python3.5.3 > Nagios XI. 
Nagios XI sends an active check to the Raspberry Pi via NRPE which runs the script check_MPH.py. The python script reads the serial port that is constantly recieving data from the arduino. The script prints out information that is sent back to the Nagios XI server and recorded. 

One of the main resaons for posting this project is to help others in creating basic custom NRPE plugins via Python. It took me quite a bit of time and research to figure this out, so I am going to condense it all to one place to hopefully help someone out.

ARDUINO:
I am going to skip the Arduino coding part because all I did there was follow the manual for my sensor to read information and then print the wind speed once every second to the serial mponitor using Serial.print(). However is is important to note the baud rate being used. It is not neccesary to use 9600 like I did, but you must use the same rate in both the python script and the Arduino script. 

PYTHON:
The port can be found in the Arduino IDE when uploading the Arduino code. Set the full path to the port to a variable. Set the baud rate to a variable (same baud rate used in Arduino). Create an object (I used 'ser' in my script) and use the function Serial() from the serial library to allow the script to read the serial port. Next I set the wind speed values that I wanted to use as warning and critical values. Use 'ser.readline()' to read the most recent line of the serial monitor and set it to an object. Then decode it by doing <your_object> = <your_object>.decode("utf-8"). Next, I looped through this 5 times and created a list of values so that I can take an average at the end. (Note that this takes 5 seconds because in the Arduino code, a new line is written every second).

EXIT CODES:
Based on the warning and critical values set at the beginning of the script, I did a series of if, elif statements to set an exit code. The exit codes are as follows: 0=OK, 1=WARNING, 2=CRITICAL, 3=UNKNOWN. Under the 'except' statement I used the sys.exit() command directly so that if an error occured, it wouldn't continue to try and find an average and get a divide by 0 error. At the end I used the sys.exit(exit_code) to close the program with the correct code. This command is essential because it is how Nagios knows the status of the service. 

PERFORMANCE DATA: 
I won't go into too much detail about this because there is a good document about how to use performance data to enable the graphs in Nagios. (https://nagios-plugins.org/doc/guidelines.html#AEN200) If you run the script from the command line, you will get an output of everything that is in quotes. However, when the output is sent to Nagios, it takes everything after the pipe, removes it, and uses it to create a graph. I have found that Nagios handles extra print statements weird, but it is possible. I didn't have a need for it in this project. 

After completeing the script, make sure to set the file to an executable file. Use the following command: 'chmod +x /path/to/your/script.py'. 

NRPE.CFG and SUDOERS:
To allow 'nagios' user to read the serial port: run the command 'sudo visudo'. Add the line 'nagios ALL = NOPASSWD:/path/to/your/script.py'. I recommend putting the plugin with all the others in /usr/local/nagios/libexec.
Open /usr/local/nagios/etc/nrpe.cfg and add the line: '[command_name]=/usr/bin/sudo /path/to/your/script.py' Note what you use as command_name as you will need this in the next step. 

NAGIOS XI:
Open the Nagios UI, navigate to CCM, and select commands. For the command line: '$USER1$/check_nrpe -H $HOSTADDRESS$ -c command_name'. Next, add a service. Use the command you just created with no arguments. I used 'xiwizard_nrpe_service' for the template. Apply configuration. You can also do all this from the command line of the Nagios server, but I have access to the UI so that made it easier. 

