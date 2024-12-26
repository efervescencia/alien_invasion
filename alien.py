import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    """Esta clase representa un alien de la flota"""

    def __init__(self, ai_game):
        """Inicializa el alien y establece su posición inicial"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #cargamos la imagen del alien y configuramos su rect
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #Iniciamos el alien cerca de la izquierda superior
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Guardamos la posición exacta del alien
        self.x = float(self.rect.x)

    def _check_edges(self):
        """Devuelve True si el alien esta en el borde o lo ha pasado"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True



    def update(self):
        """Movemos el alien hacia la derecha"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
