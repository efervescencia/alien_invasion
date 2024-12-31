import pygame.font

class Button:


    def __init__(self, ai_game, msg):
        """ Inicializamos parámetros del botón """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Configura las dimensiones y propiedades del botón
        self.width, self.height = 200, 50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        # Creamos el objeto rect del boton y lo centramos
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Solo hay que preparar el mensaje del botón na vez
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """ Convertimos msg en una imagen y centramos el texto """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        # Dibujamos un boton en blanco y luego el mensaje
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
