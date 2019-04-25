#!/usr/bin/env python3.5


import time
import RPi.GPIO as GPIO
from SteppingMode import SteppingMode
from RunningState import RunningState


class StepSequence:

    def __init__(self, n, mode):
        if n == 4 and mode == SteppingMode.FULL_STEP:
            self.sequence = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

        if n == 4 and mode == SteppingMode.HALF_STEP:
            self.sequence = [[0,0,0,1],[0,0,1,1], [0,0,1,0],[0,1,1,0],[0,1,0,0],[1,1,0,0],[1,0,0,0],[1,0,0,1]]


class StepperMotor:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    state = RunningState.STOPPED 

    def step(self):
        if self.state != RunningState.RUNNING:
            return
        self.execute_nth_step(self.pc)
        self.increment_pc()

    def execute_nth_step(self, n):
        self.execute_step(self.program[n])

#   Also used to inject a program step like [0,0,0,0]
    def execute_step(self,values):
        for (w, v) in zip(self.wires, values):
            GPIO.output(w, v)

    def increment_pc(self):
        if self.direction > 0:
            self.pc += 1
            if self.pc >= len(self.program):
                self.pc = 0
        else:
            self.pc -= 1
            if self.pc < 0:
                self.pc = len(self.program) - 1

    def run(self):
        while self.state == RunningState.RUNNING:
            self.step()
            time.sleep(self.speed / 1000.0)
    
    def start(self):
        if self.state == RunningState.STOPPED:
            self.state = RunningState.RUNNING

    def stop(self):
        self.state = RunningState.STOPPED
        # For each x in wires, lambda(x) = 0
        values = map(lambda x: 0, self.wires)
        self.execute_step(values)
        self.reset_pc()

    def pause(self):
        if self.state == RunningState.RUNNING:
            self.state = RunningState.PAUSED

    def resume(self):
        if self.state == RunningState.PAUSED:
            self.state = RunningState.RUNNING

    def reset_pc(self):
        if self.direction < 0:
            self.pc = len(self.program) - 1
        else:
            self.pc = 0

    def faster(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed += 10

    def slower(self):
        self.speed += 10
        if self.speed > 1000:
            self.speed -= 10
    

    def reverse(self):
        self.pause()
        self.direction = - self.direction
        self.resume()

    def fast_move(self, mins):
		for t = 1 to mins:
			self.step()
 		self.pause()
		

    def fast_rewind(self, mins):
        self.pause()
        self.direction = - self.direction
		saved_speed = self.speed 
		self.speed = 0
		self.fast_move(mins)
		self.speed = saved_speed
		self.direction = - self.direction
        
    def fast_forward(self, mins):
        self.pause()
		saved_speed = self.speed 
		self.speed = 0
		self.fast_move(mins)
		self.speed = saved_speed
		
    def set_speed(self, millis):
        self.pause()
        self.speed = millis 
        self.resume()
        
    def __init__(self, wires, mode, direction, speed):
        self.wires = wires
        self.mode = mode
        self.direction = direction
        self.reset_pc()
        self.program = StepSequence(len(wires), mode).sequence
        self.speed = speed

        for wire in wires:
            GPIO.setup(wire, GPIO.OUT, initial=GPIO.LOW)
