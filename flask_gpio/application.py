import os
import time
from flask import Flask
app = Flask(__name__)

import flask_gpio.control

@app.route('/turn_on')
def turn_on():
    control.turn_on();
    with open(os.path.join(os.path.dirname(app.instance_path), 'flask_gpio', 'logs', 'heater.log'), 'a') as logFile:
        logFile.write(time.strftime('[%a, %d %b %Y %H:%M:%S %Z(%z)] Turned on\n'))
    return 'Turned on'
@app.route('/turn_off')
def turn_off():
    control.turn_off();
    with open(os.path.join(os.path.dirname(app.instance_path), 'flask_gpio', 'logs', 'heater.log'), 'a') as logFile:
        logFile.write(time.strftime('[%a, %d %b %Y %H:%M:%S %Z(%z)] Turned off\n'))
    return 'Turned off'
@app.route('/view_logs')
def view_logs():
    with open(os.path.join(os.path.dirname(app.instance_path), 'flask_gpio', 'logs', 'heater.log'), 'r') as logFile:
        return logFile.read()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
