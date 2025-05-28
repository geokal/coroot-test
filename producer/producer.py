from flask import Flask, Response
import time
import random

app = Flask(__name__)

def generate_data():
    while True:
        yield f"data: {{'value': {random.randint(1, 100)}}}\n\n"
        time.sleep(1)  # simulate streaming

@app.route('/stream')
def stream():
    return Response(generate_data(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9005)
