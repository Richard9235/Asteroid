import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    updatable  = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = (updatable)

    pygame.init()
    
    AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    Player(x,y)
    clock = pygame.time.Clock()
    dt = 0
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color=(0,0,0))
        
        for i in drawable:
            i.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        
        

if __name__ == "__main__":
    main()