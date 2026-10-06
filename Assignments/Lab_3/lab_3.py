import time 
from hs3003 import HS3003

sensor = HS3003()

user = input ("""Please choose from the following options:
    T - Temperature
    H - Humidity
    0 - Both
    """) #Ask user for input
       
if user == "T":
    t, h = sensor.read() #read temperature variable
    print("Temp is: {:.1f} C".format(t)) #print temperature
if user == "H":
    t, h = sensor.read() #read humidity variable
    print("Humidity: {:.1f} %".format(h)) # humidity
if user == "0":
    t, h = sensor.read() #read temperature and humidity variables
    print("Temp: {:.1f} C   Humidity: {:.1f} %".format(t, h)) #print temperature and humidity
