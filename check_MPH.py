#!/usr/bin/python3

#Created by: Daniel Cronk
#Created on: 2/18/2019
#Last modified on: 2/26/2019
#Created for: Honda of America Mfg.
#Purpose: Read wind sensor data and send wind sensor data to Nagios Server.

import sys
import time
from math import pow
from mcp3208 import MCP3208

#set up GPIO
adc = MCP3208()
tempPin = 0
windPin = 1

warn = 6.00 #warning MPH
crit = 3.00 #critical MPH

i = 0
MPH_list = [] #used to find average of wind speed
while i < 5:
    try:
		rawMPH = float(adc.read(1))  
		convertedMPH = pow(((rawMPH - 264.0) / 85.6814), 3.36814)
        MPH_list.append(convertedMPH)

        i += 1
    except:
        print('Failed to read wind sensor')
        sys.exit(3) #unknown exit status

avgMPH = sum(MPH_list) / len(MPH_list) #average wind speed

if avgMPH > warn:
    exit_code = 0
elif avgMPH <= warn and avgMPH > crit:
    exit_code = 1
elif avgMPH <= crit:
    exit_code = 2
else:
    exit_code = 3

print("%.2f MPH | 'Wind Speed'=%.2f;%.2f;%.2f;0.0;25.0" % (avgMPH,avgMPH,warn,crit)) #speed | performance data
sys.exit(exit_code)
