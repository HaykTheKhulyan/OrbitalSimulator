import pygame
from Resources.settings import *

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    running = True
    
    clock = pygame.time.Clock()

    while (running):

        # checks the events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
