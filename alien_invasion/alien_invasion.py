import pygame # Leer: https://www.pygame.org/docs/
from pygame.sprite import Group

from settings import Settings 
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    
    pygame.init() # Inicia el juego y crea el objeto pantalla


    ai_settings = Settings() 
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # Crea un objeto
    pygame.display.set_caption("Alien Invasion - Enz0")
  
    ship = Ship(ai_settings, screen) # Se instancia una nave (objeto)

    bullets = Group() # Se instancia un objeto

    aliens = Group()

    alien = Alien(ai_settings, screen)
    
    while True: # Inicia el loop principal del juego
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)
            
run_game()
