#!/usr/bin/env python

import time
from slackclient import SlackClient
from requests import get
from sys import argv


if (len(argv)==1):
    address = "http://192.168.99.100:5556/"
else:
    address = "http://{}:5555/".format(argv[1])


# starterbot's ID as an environment variable
BOT_ID = "U65RW2JH0"

# constants
AT_BOT = "<@" + BOT_ID + ">"

# instantiate Slack & Twilio clients
slack_client = SlackClient("xoxb-209880086578-MG41GUB3R2djnqkZCMkGa4lJ")


def handle_command(command, channel):
    #Receives commands directed at the bot and sends the response

    try:
        #Requesting a response from the bot application
        response = get(address+command,timeout=2)
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=response.text, as_user=True)
    except:
        print("Error connecting to the bot application - timeout")
        print("Is {} your docker machine IP?".format(address))
        return    


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")