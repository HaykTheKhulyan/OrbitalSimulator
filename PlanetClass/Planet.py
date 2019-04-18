import pygame
import math

class Planet:

    def __init__(self, mass, radius):
        self.x_pos = 400
        self.y_pos = 400

        self.x_vel = 0
        self.y_vel = 0

        self.x_accel = 0
        self.y_accel = 0

        self.mass = mass
        self.radius = radius

    def get_mass(self):
        return self.mass
    
    def get_pos(self):
        return (self.x_pos, self.y_pos)
    
    def Update(self, star):
        self.x_accel = 0.5 * math.cos(star.get_mass() / (star.get_radius()**2))
        self.y_accel = 0.5 * math.sin(star.get_mass() / (star.get_radius()**2))

        self.x_vel += self.x_accel
        self.y_vel += self.y_accel

        self.x_pos += int(self.x_vel)
        self.y_pos += int(self.y_vel)

    def Draw(self, screen):
        pygame.draw.circle(screen, pygame.Color('black'), (self.x_pos, self.y_pos), self.radius, 0)
