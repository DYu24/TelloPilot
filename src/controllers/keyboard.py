import pygame
import tellopy
import time

class Keyboard:
    CONTROLS = {
        'up': 'forward',
        'down': 'backward',
        'left': 'left',
        'right': 'right',
        'w': 'up',
        's': 'down',
        'd': 'clockwise',
        'a': 'counter_clockwise',
        '=': lambda drone: drone.takeoff(),
        '-': lambda drone: drone.land(),
        'p': lambda drone: drone.palm_land(),
        '1': lambda drone: drone.flip_forward(),
        '2': lambda drone: drone.flip_back(),
        '3': lambda drone: drone.flip_right(),
        '4': lambda drone: drone.flip_left(),
        '5': lambda drone: drone.flip_forwardleft(),
        '6': lambda drone: drone.flip_forwardright(),
        '7': lambda drone: drone.flip_backleft(),
        '8': lambda drone: drone.flip_backright(),
    }

    def __init__(self, drone):
        self.drone = drone

    def handleInput(self, key, speed):
        print(key)
        if key in Keyboard.CONTROLS:
            action = Keyboard.CONTROLS[key]

            if type(action) == str:
                getattr(self.drone, action)(speed)
            else:
                action(self.drone)
