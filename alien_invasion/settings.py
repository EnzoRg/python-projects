# El modulo contiene la clase que almacena la configuracion 

class Settings(): # Por convencion se empieza con mayuscula 
    def __init__(self):
        # Pantalla
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (68, 71, 90)
        self.ship_speed = 3
        self.ship_limit = 3

        # Misiles de la nave
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 6
        self.bullet_color = (255, 184, 108)
        self.bullets_allowed = 3

        # Aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # -1: left