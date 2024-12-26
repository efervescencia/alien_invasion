class Settings:
    """Una clase para guardar toda la configuracion de Alien Invasion"""

    def __init__(self):
        """Inicializa la configuracion del juego"""
        # Configuracion de la pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #configuracion de la nave
        self.ship_speed = 2.5

        #Configuración de las balas
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_speed = 2.5