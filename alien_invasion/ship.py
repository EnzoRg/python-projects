import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen 
        self.ai_settings = ai_settings

        self.image = pygame.image.load('/home/blackmesa/Documentos/Python/alien_invasion/images/ship.bmp') # Carga la imagen
        self.rect = self.image.get_rect() # Crea un rectangulo que representa una nave
        self.screen_rect = screen.get_rect() # Obtiene el rectangulo que representa la pantalla del juego y lo almacena en el atributo

        # Posiciona la nave abajo al centro 
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False # Mandera para mover continuo
        self.moving_left = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        self.rect.centerx = self.center
    
    def blitme(self):
        self.screen.blit(self.image, self.rect) # Dibuja la nave en la posicion indicada 
