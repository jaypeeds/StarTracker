#!/usr/bin/env python3.5

from flask import Flask
from flask import request
import RPi.GPIO as GPIO
from StepperMotor import StepperMotor
from SteppingMode import SteppingMode
from MotorTask import MotorTask
import threading

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
stepper = StepperMotor([17,18,22,27],SteppingMode.HALF_STEP, 1, 500)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/step")
def one_step():
    stepper.step()
    return "Step: %s" % (stepper.pc)

@app.route("/start")
def motor_start():
    stepper.start()
    worker = getattr(MotorTask, 'run')
    workThead = threading.Thread(target=worker, args=[stepper])
    workThead.start()
    return "State: %s" % (stepper.state.name)

@app.route("/stop")
def motor_stop():
    stepper.stop()
    return "State: %s" % (stepper.state.name)

@app.route("/pause")
def motor_pause():
    stepper.pause()
    return "State: %s" % (stepper.state.name)

@app.route("/resume")
def motor_resume():
    stepper.resume()
    worker = getattr(MotorTask, 'run')
    workThead = threading.Thread(target=worker, args=[stepper])
    workThead.start()
    return "State: %s" % (stepper.state.name)

@app.route("/faster")
def increase_speed():
    stepper.faster()
    return "Speed: %d" % (stepper.speed)

@app.route("/slower")
def decrease_speed():
    stepper.slower()
    return "Speed: %d" % (stepper.speed)

@app.route("/reverse")
def motor_reverse():
    stepper.reverse()
    return "Direction: %d" % (stepper.direction)

@app.route("/seconds/<seconds>", methods=["POST"])
def motor_speed(seconds):
    assert seconds == request.view_args['seconds']
    stepper.set_speed(int(seconds))
    return "Speed: %d" % (stepper.speed)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

