# Using the open-source pygame library
import pygame

# Importing my own files
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

# Functions
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Creating groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    
    # Represent the middle of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    # Instantiate Player object
    player = Player(x, y)
    
    # Delta time
    dt = 0
    
    # Instantiate AsteroidField object
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        
        updateable.update(dt)
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        # Limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


# Program starts here
if __name__ == "__main__":
    main()

