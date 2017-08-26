#!/usr/bin/env python

from requests import get
from flask import Flask

#Function that checks how many intances of the bot are running
#Returns a list of their names
def get_avaliable_bots():
    chatbots=[]
    bot_id=1
    while True:
        try:
            server_link="http://chat_bot_{}:5000".format(bot_id)
            get(server_link)
            chatbots.append("bot_{}".format(bot_id))
            bot_id+=1
            
        except:
            return chatbots


#Function that handles the command and returns a string with the response
def handle_command(command):
    global connected_to

    command=command.split()
    response=""

    #User still hasn't started a session with any bot
    if not connected_to:
        if (command[0]=='list'):
            response = "\n".join(chatbots)

        elif (command[0]=='start_session'):
            if (len(command)!=2):
                response = "Not the correct format"
            else:
                bot_name = command[1]
                if bot_name in chatbots:
                    connected_to = bot_name
                    response = "You are now connected with {}".format(bot_name)
                else:
                    response = "Sorry, not available. Please type ‘list’ to see available bots"

        else:
            response = "Not a correct command" 

    #User already started a session with a bot
    else:
        if (command[0]=="end_session"):
            response = "Disconnected from {}".format(connected_to)
            connected_to = ""
        else:
            uri="http://chat_{}:5000/askmeanything/{}".format(connected_to,command[0])
            r = get(uri).json()
            response = r['response']

    return response


#Getting the list of bots
chatbots = get_avaliable_bots()
#Global variable to define to which bot it is connected
connected_to = ""


app = Flask(__name__)

#Page to request response from bot
@app.route("/<string:query>")
def get_response(query):
    return handle_command(query)

#Starting up the server
if __name__ == '__main__':
    app.run(host='0.0.0.0')

