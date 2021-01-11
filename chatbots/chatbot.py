# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 14:12:38 2020

@author: User
"""

from flask import Flask, render_template, request
from chat import chatting 

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
     if request.method == 'POST':
         user_query = request.form['user_query']
         user_query = user_query.strip()
         result = chatting(user_query)
         return render_template('index.html', response=result, user_query=user_query)
     return render_template('index.html')
 
if __name__ == "__main__":
    app.run(debug=False)
    #app.run(use_reloader=False)