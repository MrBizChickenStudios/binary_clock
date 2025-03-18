import pygame
from datetime import datetime
from constants import *
import light
import time

class Clock():
    def __init__(self):
        self.blinker_1 = []
        self.blinker_2 = []
        self.seconds = []
        self.tenth_seconds = []
        self.minutes = []
        self.tenth_minutes = []
        self.hours = []
        self.tenth_hours = []

        for i in range(1, 5):
            self.seconds.append(light.Light(PADDING * 9 + RADIUS * 9, GAME_HEIGHT - (PADDING * i + RADIUS * i), 32))

        for i in range(1, 4):
            self.tenth_seconds.append(light.Light(PADDING * 8 + RADIUS * 8, GAME_HEIGHT - (PADDING * i + RADIUS * i), 32))

        for i in range(1, 5):
            self.minutes.append(light.Light(PADDING * 6 + RADIUS * 6, GAME_HEIGHT - (PADDING * i + RADIUS * i), 32))

        for i in range(1, 4):
            self.tenth_minutes.append(light.Light(PADDING * 5 + RADIUS * 5, GAME_HEIGHT - (PADDING * i + RADIUS * i), 32))

        for i in range(1, 5):
            self.hours.append(light.Light(PADDING * 3 + RADIUS * 3, GAME_HEIGHT - (PADDING * i + RADIUS * i), 32))

        for i in range(1, 3):
            self.tenth_hours.append(light.Light(PADDING * 2 + RADIUS * 2, GAME_HEIGHT - (PADDING * i + RADIUS * i), 32))

        for i in range(1, 3):
            self.blinker_1.append(light.Light(PADDING * 4 + RADIUS * 4, GAME_HEIGHT - (PADDING * i + RADIUS * i + 100), 20))

        for i in range(1, 3):
            self.blinker_2.append(light.Light(PADDING * 7 + RADIUS * 7, GAME_HEIGHT - (PADDING * i + RADIUS * i + 100), 20))

    def update(self):
        now = datetime.now()
        current_time = now.strftime("%H%M%S")

        time = []
        for t in current_time:
            time.append(int(t))

        for light_set in [
            self.seconds, self.tenth_seconds, self.minutes,
            self.tenth_minutes, self.hours, self.tenth_hours,
            self.blinker_1, self.blinker_2
        ]:
            for light in light_set:
                light.update()

        self.show_lights(self.seconds, time[5])
        self.show_lights(self.tenth_seconds, time[4])
        self.show_lights(self.minutes, time[3])
        self.show_lights(self.tenth_minutes, time[2])
        self.show_lights(self.hours, time[1])
        self.show_lights(self.tenth_hours, time[0])


    def draw(self, surface):
        for light_set in [
            self.seconds, self.tenth_seconds, self.minutes,
            self.tenth_minutes, self.hours, self.tenth_hours,
            self.blinker_1, self.blinker_2
        ]:
            for light in light_set:
                light.draw(surface)

    def show_lights(self, lights, num):
        bit_length = len(lights)
        bit_values = [2**i for i in range(bit_length)][::-1]
        output = [0] * bit_length

        for i in range(bit_length):
            if num >= bit_values[i]:
                output[i] = 1
                num -= bit_values[i]

        output.reverse()

        for i in range(bit_length):
            lights[i].on = bool(output[i])
