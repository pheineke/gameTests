import random
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

players = {}
bushes = []

# Weltgrößen
WORLD_WIDTH = 2000
WORLD_HEIGHT = 2000

# Anzahl der Büsche
NUM_BUSHES = 1000

# Generiere zufällige Büsche in der Welt
def generate_bushes():
    global bushes
    bushes = []
    for _ in range(NUM_BUSHES):
        bushes.append(
            {'x': random.randint(0, WORLD_WIDTH) + random.randint(5, 100), 
             'y': random.randint(0, WORLD_HEIGHT) + random.randint(5, 100),
             'size': random.randint(50, 100)}
        )

generate_bushes()


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('init_bushes', bushes)

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
    # Handle player disconnection logic here

@socketio.on('player_move')
def handle_player_move(data):
    player_id = data['id']
    players[player_id] = data['position']
    emit('update_positions', players, broadcast=True)

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', debug=True)
