#!/usr/bin/env python

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask,jsonify


#Setting up the chat bot

chatbot = ChatBot('bot')

conversation = [
    "What",
    "Sky is blue",
    "How",
    "Roses are red",
    "Hello",
    "What do you want?",
    "End",
    "Don't leave me now"
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)


#Setting up de Flask server
#This bot uses port 5001

app = Flask(__name__)
#Default page for the Flask server
@app.route("/")
def home():
    return "You are now connected with the bot"

#Page to request response from bot
@app.route("/askmeanything/<string:query>")
def get_response(query):
    response=str(chatbot.get_response(query))
    return jsonify({'response':response})

#Starting up the server
if __name__ == '__main__':
    app.run(host='0.0.0.0')

