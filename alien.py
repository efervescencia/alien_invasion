import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Esta clase representa un alien de la flota"""

    def __init__(self, ai_game):
        """Inicializa el alien y establece su posición inicial"""
        super().__init__()
        self.screen = ai_game.screen

        #cargamos la imagen del alien y configuramos su rect
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #Iniciamos el alien cerca de la izquierda superior
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Guardamos la posición exacta del alien
        self.x = float(self.rect.x)

