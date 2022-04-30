#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:02:48 2022

@author: hugh
"""

class Vehicle():
    def __init__(self):
        self.ignition = False
        self.throttle = 0
        self.steering = 0
        self.visual_warning = False
        self.auditory_warning = False
        self.involuntary_assist = False
    
    def start_ignition(self):
        self.ignition = True
        
    def stop_ignition(self):
        self.ignition = False
        
    def accelerate(self):
        self.throttle = self.throttle + 5
        
    def floor_it(self):
        self.throttle = 100
        
    def decelerate(self):
        self.throttle = self.throttle - 5
        
    def no_pedal(self):
        self.throttle = 0
        
    def cruise(self):
        self.throttle = 10
        
    def steer_left(self):
        self.steering = self.steering - 10
        

    def steer_right(self):
        self.steering = self.steering + 10  
        
    def visual(self):
        self.visual_warning = True
        
    def auditory(self):
        self.auditory_warning = True
        
    def assist(self):
        self.involuntary_assist = True

        