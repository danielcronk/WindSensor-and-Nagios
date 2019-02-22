#!/usr/bin/python3

import serial
import sys
import time

port = '/dev/ttyACM0'
baud = 9600

ser = serial.Serial(port,baud)
time.sleep(1) #allow time to connect with serial
warn = 1.00 #warning MPH
crit = 15.00 #critical MPH

i = 0
MPH_list = [] #used to find average of wind speed
while i < 5:
    try:
        speed = ser.readline()
        speed = speed.decode("utf-8")
        MPH_list.append(float(speed))

        i += 1
    except:
        print('Failed to read Serial Monitor')
        sys.exit(3) #unknown exit status

avgMPH = sum(MPH_list) / len(MPH_list) #average wind speed

if avgMPH < warn:
    exit_code = 0
elif avgMPH >= warn and avgMPH < crit:
    exit_code = 1
elif avgMPH >= crit:
    exit_code = 2
else:
    exit_code = 3

print("%.2f MPH | 'Wind Speed'=%.2f;%.2f;%.2f;0.0;150.0" % (avgMPH,avgMPH,warn,crit)) #speed | performance data
sys.exit(exit_code) 
