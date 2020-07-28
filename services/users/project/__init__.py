import os
from flask import Flask,jsonify


app= Flask(__name__)

#set config
app_config=os.getenv('APP_SETTINGS') 
app.config.from_object(app.config)

@app.route('/users/ping')
def ping_pong():
    return jsonify({
        'status':'Success',
        'Message':'pong !'
    })

    