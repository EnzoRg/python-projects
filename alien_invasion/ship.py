import pygame

class Ship():

    def __init__(self, ai_game):
        self.screen = ai_game.screen 
        self.settings = ai_game.settings 
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('alien_invasion/images/ship_001.bmp')
        self.rect = self.image.get_rect()   # Crea un rectangulo que representa una nave

        

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def blittime(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

        #self.ai_settings = ai_settings

         # Carga la imagen
         
        #self.screen_rect = screen.get_rect() # Obtiene el rectangulo que representa la pantalla del juego y lo almacena en el atributo

        # Posiciona la nave abajo al centro 
        #self.rect.centerx = self.screen_rect.centerx 
        #self.rect.bottom = self.screen_rect.bottom

        #self.center = float(self.rect.centerx)

        #self.moving_right = False # Mandera para mover continuo
        #self.moving_left = False
    
    #def update(self):
        #if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.center += self.ai_settings.ship_speed_factor
        #if self.moving_left and self.rect.left > 0:
            #.center -= self.ai_settings.ship_speed_factor
        
        #self.rect.centerx = self.center
    
    #def blitme(self):
        #self.screen.blit(self.image, self.rect) # Dibuja la nave en la posicion indicada 
