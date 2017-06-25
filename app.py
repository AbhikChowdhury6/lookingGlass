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
    emotion = data['emotion']
    for p in emotion:
        if p == 'happy':h=h+1
        if p == 'sad':s=s+1
        if p == 'angry':an=an+1
        if p == 'afraid':af=af+1
        if p == 'neutral':n=n+1
        if p == 'suprised':su=su+1
        if p == 'disgusted':di=di+1
    happy_per = (h/(h+s+an+af+n+su+di))*100
    sad_per = (s/(h+s+an+af+n+su+di))*100
    angry_per = (an/(h+s+an+af+n+su+di))*100
    afraid_per = (af/(h+s+an+af+n+su+di))*100
    neutral_per = (n/(h+s+an+af+n+su+di))*100
    sup_per = (su/(h+s+an+af+n+su+di))*100
    disu_per = (di/(h+s+an+af+n+su+di))*100
    if (happy_per+sup_per+neutral_per>sad_per+afraid_per+disu_per): mood = 'Engaged'
    else: mood = 'Bored' 
    print("Percentage of people Happy %s\n Percentage of people Neutral %s \n Percentage of people Suprised %s \n Percentage of people Afraid %s \n Percentage of people sad %s \n Percentage of people sad %s \n THE PEOPLE IN THE ROOM ARE %s \n" % (happy_per,neutral_per,sup_per,afraid_per,sad_per,sad_per,mood) )
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
