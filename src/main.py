import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Class manages assets & game behaviour"""

    def __init__(self):
        """Initialize game & resources"""

        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.bg_color = self.settings.background_color
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Begin game loop"""
        
        while True:
            #Get key & mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #redraw screen elements
            self.screen.fill(self.bg_color)

            #display most recently drawn screen
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()