#!/usr/bin/env python3.5

from flask import Flask
import RPi.GPIO as GPIO
from StepperMotor import StepperMotor
from SteppingMode import SteppingMode
from MotorTask import MotorTask
import threading

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
stepper = StepperMotor([17,18,22,27],SteppingMode.FULL_STEP, 1, 500)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/on")
def led_on():
    GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
    GPIO.output(17, GPIO.HIGH)
    return "on"

@app.route("/off")
def led_off():
    GPIO.setup(17, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)
    return "off"

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

if __name__ == "__main__":
    app.run(host='0.0.0.0')

