import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys 
from shot import *

def main():
    #GROUPS
    updatable  = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #CONTAINERS
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (drawable,shots,updatable)

    #Initializing Game
    pygame.init()
    
    #Variables
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    #OBJECTS
    AsteroidField()
    player = Player(x,y)
    clock = pygame.time.Clock()


    
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
        for i in asteroids:
            if i.collisions(player) == True:
                print("Game over!")
                sys.exit()
        for i in asteroids:
            for n in shots:
                if i.collisions(n):
                    i.split(dt)
                    n.kill()
        

if __name__ == "__main__":
    main()