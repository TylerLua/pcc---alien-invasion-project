import pygame

class Ship:
    """Class handles the ship (player)"""
    
    def __init__(self, ai_game):
        """Initialize the ship & starting position"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image
        self.image = pygame.image.load("assets\ship.bmp")
        self.rect = self.image.get_rect()

        #Place ship at bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)