import flask
import flask_socketio
import redis

app = flask.Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
socketio = flask_socketio.SocketIO(app, cors_allowed_origins="*")
r = redis.Redis(host='192.168.1.123', port=30002)

@app.route("/")
def index():
    return flask.render_template("index.html")

@socketio.on("update_left")
def update_left(data):
    r.publish('motor_left', int(data['value'])/100)

@socketio.on("update_right")
def update_right(data):
    r.publish('motor_right', int(data['value'])/100)

if __name__ == '__main__':
    print('starting')
    socketio.run(app, host='0.0.0.0', port=5000)