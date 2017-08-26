#!/usr/bin/env python

from requests import get
from sys import argv

if (len(argv)==1):
    address = "http://192.168.99.100:5556/"
else:
    address = "http://{}:5555/".format(argv[1])

#Getting user input
while True:
    try:
        command=input(">@tellme ")

    except(KeyboardInterrupt, EOFError, SystemExit):
        print("\nThank you, bye!")
        break

    if (len(command)==0):
        continue

    try:
        #Requesting a response from the bot application
        response = get(address+command,timeout=2)
        print(response.text)

    except:
        print("Error connecting to the bot application - timeout")
        print("Is {} your docker machine IP?".format(address))
        break