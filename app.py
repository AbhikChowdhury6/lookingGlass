from flask import Flask, request, current_app
import json
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return current_app.send_static_file('hi.html')
    #return 'hi'

#recive json for video
#parse into objects
#stream into client

#recive json for
#j = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
#print j['two']

#recive json for speaker sentement
@app.route('/vid/', methods=['POST'])
def recieveVideoUpdates():
    data = request.get_json()
    print data
    #print data['name']
    #print data['cars'][1]['models'][2]
    return "ok"

@app.route('/atex/', methods=['POST'])
def recieveAudioEmotion():
    data = request.get_json()

@app.route('/aemo/', methods=['POST'])
def recieveAudioSentemint():
    data = request.get_json()

if __name__ == '__main__':
  socketio.run(app)
