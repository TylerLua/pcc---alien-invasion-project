import sys
import pygame

class AlienInvasion:
    """Class manages assets & game behaviour"""

    def __init__(self):
        """Initialize game & resources"""
        
        GAME_WIDTH = 1200
        GAME_HEIGHT = 800

        pygame.init()

        self.screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Begin game loop"""
        
        while True:
            #Get key & mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #display most recently drawn screen
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()