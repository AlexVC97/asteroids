# Using the open-source pygame library
import pygame

# Importing my own files
from constants import *

# Functions
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()
        
        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000




# Program starts here
if __name__ == "__main__":
    main()

