import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(F"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(F"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()

        # Get out of the game loop if needed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
            
        # Update
        player.update(dt)

        # Render
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # Wait
        dt = clock.tick(60) / 1000
        print(F"Update dt:{dt}")

if __name__ == "__main__":
    main()
