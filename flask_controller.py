from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, send

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"]) # Client http
app.config['CORS HEADERS'] = 'Content-Type'
socketio = SocketIO(app)

@app.route('/')
def handle_message():
    return "Hello world"

# @socketio.on('message')
# def handle_message(msg):
#     print("Message: ", msg)

@socketio.on('message')
def handle_message(msg):
    print("Received message:", msg)
    # Simulate a time-consuming task (replace this with your actual task)
    import time
    time.sleep(5)
    result = "Task completed: " + msg
    print("Sending result:", result)
    socketio.emit('result', {'data': result})

if __name__ == '__main__':
    # app.run(debug = True)
    socketio.run(app)