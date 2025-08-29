import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Class manages assets & game behaviour"""

    def __init__(self):
        """Initialize game & resources"""

        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.bg_color = self.settings.background_color
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Begin game loop"""
        
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)   

    def _check_events(self):
        """Responds to keypresses/mouse event"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
         """Update images and flip to new screen"""
         self.screen.fill(self.bg_color)
         self.ship.blitme()
         pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()