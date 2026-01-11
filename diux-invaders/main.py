import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(F"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(F"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")
    
    # Init Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Prepare Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Init game state
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        log_state()

        # Get out of the game loop if needed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
            
        # Update
        updatable.update(dt)

        # Check collisions
        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
    
        # Render
        screen.fill("black")

        # Render drawables
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        # Wait
        dt = clock.tick(60) / 1000
        print(F"Update dt:{dt}")

if __name__ == "__main__":
    main()
