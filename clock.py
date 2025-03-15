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
            self.seconds.append(light.Light(PADDING * 9 + RADIUS * 9, PADDING * i + RADIUS * i, 32))
        for i in range(1, 4):
            self.tenth_seconds.append(light.Light(PADDING * 8 + RADIUS * 8, PADDING * i + RADIUS * i, 32))
        for i in range(1, 5):
            self.minutes.append(light.Light(PADDING * 6 + RADIUS * 6, PADDING * i + RADIUS * i, 32))
        for i in range(1, 4):
            self.tenth_minutes.append(light.Light(PADDING * 5 + RADIUS * 5, PADDING * i + RADIUS * i, 32))
        for i in range(1, 5):
            self.hours.append(light.Light(PADDING * 3 + RADIUS * 3, PADDING * i + RADIUS * i, 32))
        for i in range(1, 3):
            self.tenth_hours.append(light.Light(PADDING * 2 + RADIUS * 2, PADDING * i + RADIUS * i, 32))

        for i in range(1, 3):
            self.blinker_1.append(light.Light(PADDING * 4 + RADIUS * 4, PADDING * i + RADIUS * i + 100, 20))

        for i in range(1, 3):
            self.blinker_2.append(light.Light(PADDING * 7 + RADIUS * 7, PADDING * i + RADIUS * i + 100, 20))


    def update(self):
        # Get current time
        current_time = time.localtime()
        seconds = current_time.tm_sec
        minutes = current_time.tm_min
        hours = current_time.tm_hour

        for light in self.seconds:
            light.update()

        for light in self.tenth_seconds:
            light.update()

        for light in self.minutes:
            light.update()

        for light in self.tenth_minutes:
            light.update()

        for light in self.hours:
            light.update()

        for light in self.tenth_hours:
            light.update()

        for light in self.blinker_1:
            light.update()

        for light in self.blinker_2:
            light.update()


        self.show_lights(self.seconds, seconds // 4)
        self.show_lights(self.tenth_seconds, seconds % 4)

        self.show_lights(self.minutes, minutes // 4)
        self.show_lights(self.tenth_minutes, minutes % 4)

        self.show_lights(self.hours, hours // 4)
        self.show_lights(self.tenth_hours, hours % 4)

        self.show_lights(self.blinker_1,0)
        self.show_lights(self.blinker_2, 0)

    def draw(self, surface):
        for second in self.seconds:
            second.draw(surface)

        for tenth_second in self.tenth_seconds:
            tenth_second.draw(surface)

        for minute in self.minutes:
            minute.draw(surface)

        for tenth_minute in self.tenth_minutes:
            tenth_minute.draw(surface)

        for hour in self.hours:
            hour.draw(surface)

        for tenth_hour in self.tenth_hours:
            tenth_hour.draw(surface)

        for light in self.blinker_1:
            light.draw(surface)

        for light in self.blinker_2:
            light.draw(surface)

    def show_lights(self, lights, num):
        bit = [8, 4, 2, 1]
        output = []

        for b in bit:
            if num >= b:
                output.append(1)
                num -= b
            else:
                output.append(0)


        output = output[:len(lights)]

        for i in range(len(output)):
            if output[i] == 1:
                lights[i].on = True
            else:
                lights[i].on = False

            
