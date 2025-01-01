class Settings:
    """Una clase para guardar toda la configuracion de Alien Invasion"""

    def __init__(self):
        """Inicializa la configuracion del juego"""
        # Configuracion de la pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        self.ships_limit = 3

        #Configuración de las balas
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10
        self.bullet_width = 5
        self.bullet_height = 10

        self.fleet_drop_speed = 10
        """Fleet direction = 1 representa derecha, -1 representa izquierda"""
        self.fleet_direction = 1
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1

        # lo rápido que aumenta el valor en puntos de los aliens
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        #configuración del alien
        self.alien_speed = 1.0
        #configuracion de la nave
        self.ship_speed = 2.5
        #configuracion de las balas
        self.bullet_speed = 2.5

        #puntuación
        self.alien_points = 50


    def increase_speed(self):
        """Incrementamos las configuraciones de velocidad."""
        self.alien_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
