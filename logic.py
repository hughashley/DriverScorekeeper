#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:04:20 2022

@author: hugh
"""

class scorekeeper():
    def __init__(self):
        self.driver_score = .5
        self.driver_skill = 'Average'
        
    def logic_kernel(self):
        if self.driver_score >= .85:
            self.driver_skill = 'Excellent'
        elif self.driver_score >= .55 and self.driver_score <= .84:
            self.driver_skill = 'Good'
        elif self.driver_score >= .40 and self.driver_score <= .54:
            self.driver_skill = 'Average'
        elif self.driver_score >= .20 and self.driver_score <= .39:
            self.driver_skill = 'Fair'
        elif self.driver_score <= .19:
            self.driver_skill = 'Poor'
            
    def smallDeduction(self):
        self.driver_score = self.driver_score - .01
        
    def largeDeduction(self):
        self.driver_score = self.driver_score - .05
        
    def driverImprovement(self):
        self.driver_score = self.driver_score + .05