#!/usr/bin/env python3.5

from StepperMotor import StepperMotor

class MotorTask:

    def __init__(self, stepper):
        self.stepper = stepper

    def start(self):
        self.stepper.run()       

    def run(stepper):
       stepper.run() 
