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

        #Movement flag; start with ship not moving
        self.moving_right = False
        self.moving_left = False

        #Store a float value for precice ship movement
        self.x = float(self.rect.x)

        #Ship settings
        self.settings = ai_game.settings
        
    def update(self):
        """Update ships position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update ship rect x from self x
        self.rect.x = self.x

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image, self.rect)