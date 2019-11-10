from flask import Flask
import flask
import time
import threading
import requests
from TimeDefiner import TimeDefiner


time_definer = TimeDefiner()
app = Flask(__name__)

VALUE = None
UPDATE_DATA_TIME = 30
LAST_REQUEST_TIME = None

@app.route('/')
def index():
    global VALUE, LAST_REQUEST_TIME

    while not VALUE:
        time.sleep(0.1)

    resp = flask.Response(VALUE)
    max_age = (time.time() - LAST_REQUEST_TIME) // 1 + 1
    resp.headers['Cache-Control'] = 'max-age={}, must-revalidate'.format(int(max_age))
    return resp


def updating_data():
    global VALUE, UPDATE_DATA_TIME, LAST_REQUEST_TIME
    while True:
        now = time.time()
        response = requests.get('http://localhost:5001')
        request_time = time.time() - now
        VALUE = response.text
        LAST_REQUEST_TIME = time.time()

        next_request_time = time_definer.get_next_wait_time(request_time)
        time.sleep(UPDATE_DATA_TIME - next_request_time)


if __name__ == "__main__":
    updating = threading.Thread(target=updating_data)
    updating.start()
    app.run()
