from flask import Flask
import time

app = Flask(__name__)

start_point = time.time()

@app.route('/')
def index():
    time.sleep(2)
    value = (time.time() - start_point) // 5
    return str(value)


if __name__ == "__main__":
    app.run(port=5001)
