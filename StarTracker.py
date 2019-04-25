#!/usr/bin/env python3.5

from flask import Flask, request, render_template
from StepperMotor import StepperMotor
from SteppingMode import SteppingMode
from MotorTask import MotorTask
import logging
import threading

app = Flask(__name__)
# Somewhat noisier
# stepper = StepperMotor([17,18,22,27],SteppingMode.FULL_STEP, 1, 150)
# Some heat with half-step
stepper = StepperMotor([17,18,22,27],SteppingMode.HALF_STEP, 1, 75)

@app.route("/step")
def one_step():
    stepper.step()
    return "{'%s':'%d'}" % ("pc", stepper.pc)

@app.route("/start")
def motor_start():
    stepper.start()
    worker = getattr(MotorTask, "run")
    workThead = threading.Thread(target=worker, args=[stepper])
    workThead.start()
    return "{'%s':'%s'}" % ("state", stepper.state.name) #, 204

@app.route("/stop")
def motor_stop():
    stepper.stop()
    return "{'%s':'%s'}" % ("state", stepper.state.name) #, 204

@app.route("/pause")
def motor_pause():
    stepper.pause()
    return "{'%s':'%s'}" % ("state", stepper.state.name) #, 204

@app.route("/resume")
def motor_resume():
    stepper.resume()
    worker = getattr(MotorTask, 'run')
    workThead = threading.Thread(target=worker, args=[stepper])
    workThead.start()
    return "{'%s':'%s'}" % ("state", stepper.state.name) #, 204

@app.route("/faster")
def increase_speed():
    stepper.faster()
    return "{'%s':'%d'}" % ("speed", stepper.speed) #, 204

@app.route("/slower")
def decrease_speed():
    stepper.slower()
    return "{'%s':'%d'}" % ("speed", stepper.speed) #, 204

@app.route("/reverse")
def motor_reverse():
    stepper.reverse()
    return "{'%s':'%d'}" % ("direction", stepper.direction) #, 204

@app.route("/fast_rewind/<mins>", methods=["POST"])
def motor_rewind():
	assert mins == request.view_args['mins']
    stepper.fast_rewind(mins)
    return "{'%s':'%d'}" % ("rewind", mins) #, 204

@app.route("/fastforward/<mins>", methods=["POST"])
def motor_rewind():
	assert mins == request.view_args['mins']
    stepper.fast_forward(mins)
    return "{'%s':'%d'}" % ("fast_forward", mins) #, 204

@app.route("/speed/<millis>", methods=["POST"])
def motor_speed(millis):
    assert millis == request.view_args['millis']
    stepper.set_speed(int(millis))
    return "{'%s':'%d'}" % ("speed", stepper.speed) #, 204

@app.route('/<string:page_name>/')
def render_static(page_name):
        return render_template('%s.html' % page_name) #, 204

if __name__ == "__main__":
    logger = logging.getLogger("werkzeug")
    handler = logging.FileHandler("access.log")
    logger.addHandler(handler)

    # Also add the handler to Flask's logger for cases
    #  where Werkzeug isn't used as the underlying WSGI server.
    app.logger.addHandler(handler)
    #app.run(debug=True)
    app.run()

