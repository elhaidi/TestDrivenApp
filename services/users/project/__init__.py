from flask import Flask,jsonify


app= Flask(__name__)

#set config
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/users/ping')
def ping_pong():
    return jsonify({
        'status':'Success',
        'Message':'pong !'
    })

    