# El modulo contiene la clase que almacena la configuracion 

class Settings(): # Por convencion se empieza con mayuscula 
    def __init__(self):
        # Pantalla
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (68, 71, 90)

        self.ship_limit = 3

        # Misiles de la nave

        self.bullet_width = 3
        self.bullet_height = 6
        self.bullet_color = (255, 184, 108)
        self.bullets_allowed = 3

        # Aliens
        self.fleet_drop_speed = 10
        self.score_scale = 1.5

        self.speedup_scale = 1.2
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 3 
        self.bullet_speed = 2.5      
        self.alien_speed = 1.0
        self.fleet_direction = 1 # -1: left
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)