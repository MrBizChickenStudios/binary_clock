import pygame
import random
from constants import *

class Light():
    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.on = False

        self.on_color = (255, 0, 0)
        self.off_color = (40, 0, 0)
        self.color = self.off_color

    def update(self):
        self.color = self.on_color if self.on else self.off_color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)  # Draw the circle
