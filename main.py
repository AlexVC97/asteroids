# Using the open-source pygame library
import pygame

# Importing my own files
from constants import *

# Functions
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()




# Program starts here
if __name__ == "__main__":
    main()

