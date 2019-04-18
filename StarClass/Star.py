import pygame

from Resources.settings import *

class Star:

    def __init__(self, mass, radius):
        self.x_pos = int(WINDOW_WIDTH / 2)
        self.y_pos = int(WINDOW_HEIGHT / 2)

        self.mass = mass
        self.radius = radius
    
    def get_mass(self):
        return self.mass
        
    def get_radius(self):
        return self.radius
    
    def get_pos(self):
        return (self.x_pos, self.y_pos)

    def Draw(self, screen):
        pygame.draw.circle(screen, pygame.Color('black'), (self.x_pos, self.y_pos), self.radius, 0)
