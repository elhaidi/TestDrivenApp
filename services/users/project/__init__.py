from flask import Flask,jsonify


app= Flask(__name__)

@app.route('/users/ping')
def ping_pong():
    return jsonify({
        'status':'Success',
        'Message':'pong !'
    })

    