# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:12:38 2020

@author: User
"""

from flask import Flask, render_template, request, jsonify
from chat import chatting 

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
     return render_template('chat.html')

@app.route("/chat", methods=['GET', 'POST'])
def chat():
    user_query = request.json
    print(user_query)
    user_query = user_query['name']
    result = chatting(user_query)
    print(result)
    return jsonify(result)
if __name__ == "__main__":
    app.run(debug=False)
    app.run(use_reloader=False)
    
