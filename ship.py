import  pygame

class Ship:
    """Una clase para gestionar la nave"""


    def __init__(self, ai_game):
        """iniializo la nave y configuro su posicion inicial"""
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Coloca inicialmente cada nave nueva en el centro de la parte inferior de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom

        #guardamos un valor decimal para la posicion horizontal de la nave
        self.x = float(self.rect.x)

        #banderas de movimiento
        self.moving_right = False
        self.moving_left = False


    def blitme(self):
        """Dibuja la anve en su ubicacion actual"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        #actualizamos el objeto rect
        self.rect.x = self.x


    def center_ship(self):
        """Centra la nave en la pantalla"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)