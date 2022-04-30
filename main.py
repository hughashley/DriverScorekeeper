#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 17:04:31 2022

@author: hugh
"""

import pygame
import vehicle
import logic

class controller():
    def __init__(self):
        self.scores = logic.scorekeeper()
        self.jeep = vehicle.Vehicle()
        pygame.init()
        res = (700,400)
        screen = pygame.display.set_mode(res)
        color_light = (170,170,170)
        color_dark = (100,100,100)
        pygame.display.set_caption("Team EvoSquad")
        font = pygame.font.SysFont('Corbel', 35)
        throttle_label = 'throttle: '
        acceleration_label = 'acceleration: '
        speed_label = 'speed: '
        previous_frame_time = 0
        speed = 0
        acceleration = 0
        init = True
        visual_start = 0
        auditory_start = 0
        assist_start = 0
        while True:

            frame_throttle = self.jeep.throttle
            if frame_throttle < 0:
                frame_throttle = 0
            elif frame_throttle > 100:
                frame_throttle = 100

            
            current_frame_time = pygame.time.get_ticks()/1000
            if frame_throttle == 0:
                pass
            elif frame_throttle > 0 and frame_throttle <= 24:
                acceleration = 0
            elif frame_throttle >= 25 and frame_throttle <= 30:
                acceleration = 1.5
            elif frame_throttle >= 31 and frame_throttle <= 45:
                acceleration = 2.8
            elif frame_throttle >= 46 and frame_throttle <= 60:
                acceleration = 4.0
            elif frame_throttle >= 61 and frame_throttle <= 75:
                acceleration = 5.3
            elif frame_throttle >= 76 and frame_throttle <= 85:
                acceleration = 6.7
            elif frame_throttle >= 86 and frame_throttle <= 99:
                acceleration = 7.4
            elif frame_throttle == 100:
                acceleration = 10.0

               
            if acceleration == 0:
                pass
            elif acceleration <= -50:
                acceleration = -50
            elif acceleration >= 10:
                acceleration = 10
                
                
            delta_t = current_frame_time - previous_frame_time
            
            if frame_throttle == 0 and speed > 0 and init == False and acceleration >0:
                acceleration = (acceleration * -1)

            speed = speed + (acceleration*delta_t)
            
            if frame_throttle == 0 and speed == 0:
                acceleration = 0
            
            if speed >= 200.00:
                frame_throttle = 10
                speed = 200
                acceleration = 0
            elif speed < 0:
                speed = 0
            elif speed > 140:
                start_time = pygame.time.get_ticks()
                
            if self.scores.driver_score <= 0:
                self.scores.driver_score = 0
            
            if self.jeep.steering < -10 and acceleration > 4 or self.jeep.steering < -10 and speed > 140:
                self.scores.smallDeduction()
                self.warning()
            elif self.jeep.steering > 10 and acceleration > 4 or self.jeep.steering > 10 and speed > 140:
                self.scores.smallDeduction()
                self.warning()
            elif self.jeep.steering < -20 and acceleration > 4 or self.jeep.steering > -20 and speed > 140:
                self.scores.smallDeduction()
                self.warning()
            elif self.jeep.steering > 20 and acceleration > 4 or self.jeep.steering > 20 and speed > 140:
                self.scores.smallDeduction()
                self.warning()
                
            
            previous_frame_time = current_frame_time
            
            throttle = font.render((str(throttle_label) + str(frame_throttle) + ' %'), True, color_dark, color_light)
            throttle_rect = throttle.get_rect()
            throttle_rect.midleft = (20,20)
            
            acceleration_out = font.render((str(acceleration_label) + str(acceleration) + ' m/s/s'), True, color_dark, color_light)
            acceleration_rect = acceleration_out.get_rect()
            acceleration_rect.midleft = (20,45)
        
            speed_out = font.render((str(speed_label) + str(format(speed,'.2f')) + ' km/h'), True, color_dark, color_light)
            speed_rect = speed_out.get_rect()
            speed_rect.midleft = (20,70)
            
            driver_score = font.render('driver score: ' + str(format(self.scores.driver_score, '.2f') + ' (range of 0.0-1.0)'), True, color_dark, color_light)
            score_rect = driver_score.get_rect()
            score_rect.midleft = (20,105)
            
            driver_skill = font.render('driver skill: ' + str(self.scores.driver_skill), True, color_dark, color_light)
            skill_rect = driver_skill.get_rect()
            skill_rect.midleft = (20,140)
            
            steer = font.render('Steering position: ' + str(self.jeep.steering) + ' negative is left, positive is right', True, color_dark, color_light)
            steering_rect = steer.get_rect()
            steering_rect.midleft = (20,175)

            visual = font.render('VISUAL WARNING', True, (255,0,0), color_light)
            visual_rect = visual.get_rect()
            visual_rect.midleft = (20,210)
            
            auditory = font.render('AUDITORY WARNING', True, (255,0,0), color_light)
            auditory_rect = auditory.get_rect()
            auditory_rect.midleft = (20,245)
            
            assist = font.render('INVOLUNTARY ASSIST', True, (255,0,0), color_light)
            assist_rect = assist.get_rect()
            assist_rect.midleft = (20,280)
                              
            
            
            self.scores.logic_kernel()
            
            events = pygame.event.get()
            
            for event in events:
          
                if event.type == pygame.QUIT:
                    pygame.quit()
              
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.jeep.accelerate()
                    if event.key == pygame.K_DOWN:
                        self.jeep.decelerate()
                    if event.key == pygame.K_LEFT:
                        self.jeep.steer_left()
                    if event.key == pygame.K_RIGHT:
                        self.jeep.steer_right()
                    if event.key == pygame.K_n:
                        self.jeep.no_pedal()
                    if event.key == pygame.K_c:
                        self.jeep.cruise()
                    if event.key == pygame.K_a:
                        self.jeep.auditory()
                    if event.key == pygame.K_v:
                        self.jeep.visual()
                    if event.key == pygame.K_z:
                        self.jeep.assist()
                    if event.key == pygame.K_u:
                        self.scores.driverImprovement()
                    if event.key == pygame.K_d:
                        self.scores.largeDeduction()
                    if event.key == pygame.K_f:
                        self.jeep.floor_it()
                        self.scores.smallDeduction()
                        self.warning()
                    if event.key == pygame.K_SPACE:
                        self.jeep.no_pedal()
                        if speed < 15:
                            acceleration = -25
                    if event.key == pygame.K_s:
                        self.jeep.no_pedal()
                        self.scores.largeDeduction()
                        self.warning()
                        if speed < 15:
                            acceleration = -50
                        else:
                            acceleration = -50
                            self.scores.smallDeduction()
                            self.warning()

            if speed == 0:
                if frame_throttle == 0:
                    acceleration = 0
            screen.fill(color_light)

            if self.jeep.visual_warning == True:
                screen.blit(visual, visual_rect)
                if visual_start == 0:
                    visual_start = current_frame_time
                elif current_frame_time - visual_start > 3:
                    visual_start = 0
                    self.jeep.visual_warning = False
            if self.jeep.auditory_warning == True:
                screen.blit(auditory, auditory_rect)
                if auditory_start == 0:
                    auditory_start = current_frame_time
                elif current_frame_time - auditory_start > 3:
                    auditory_start = 0
                    self.jeep.auditory_warning = False                
            if self.jeep.involuntary_assist == True:
                screen.blit(assist, assist_rect)
                if assist_start == 0:
                    assist_start = current_frame_time
                elif current_frame_time - assist_start > 3:
                    assist_start = 0
                    self.jeep.involuntary_assist = False    
                
            screen.blit(throttle, throttle_rect)
            screen.blit(acceleration_out, acceleration_rect)
            screen.blit(speed_out, speed_rect)
            screen.blit(driver_score, score_rect)
            screen.blit(driver_skill, skill_rect)
            screen.blit(steer, steering_rect)

            pygame.display.update()
            init = False
            
            
    def warning(self):
        if self.scores.driver_skill == 'Poor':
            self.jeep.visual()
            self.jeep.auditory()
            self.jeep.assist()
        elif self.scores.driver_skill == 'Fair':
            self.jeep.visual()
            self.jeep.auditory()
            self.jeep.assist()
        elif self.scores.driver_skill == 'Average':
            self.jeep.visual()
            self.jeep.auditory()
        elif self.scores.driver_skill == 'Good':
            self.jeep.visual()
        elif self.scores.driver_skill == 'Excellent':
            self.jeep.visual()
        
if __name__ =='__main__':
    run = controller()
    