# main.py - reads the sensor and prints the values
# Needs hs3003.py uploaded to the board as well.

import time 
from hs3003 import HS3003

sensor = HS3003()

while True:
    t, h = sensor.read() #temperature and humidity variables
    print("Temp: {:.1f} C   Humidity: {:.1f} %".format(t, h)) #print temperature and humidity
    time.sleep(2) # wait 2 seconds
    if t>32: #if temperature is greater than 32 
        print("The temperature is high.")
    if t<10: #if temperature is less than 10
        print("The temperature is low.")
    else: #if temperature is between 11 and 31
        print("The temperature is normal.")

