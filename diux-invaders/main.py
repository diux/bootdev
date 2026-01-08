import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(F"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(F"Screen width: {SCREEN_WIDTH}")
    print(F"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()

        # Get out of the game loop if needed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  

        screen.fill("black")
        pygame.display.flip()

    

if __name__ == "__main__":
    main()
