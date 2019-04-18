import pygame

from Resources.settings import *
from StarClass.Star import Star
from PlanetClass.Planet import Planet

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(pygame.Color('white'))

    running = True



    sun = Star(100, 20)
    earth = Planet(10, 5)



    clock = pygame.time.Clock()

    while (running):

        # checks the events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        screen.fill(pygame.Color('white'))

        earth.Update(sun)
        
        sun.Draw(screen)
        earth.Draw(screen)
                
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
