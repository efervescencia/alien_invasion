import pygame.font


class Scoreboard:
    """La clase para la información de la puntuación"""


    def __init__(self, ai_game):
        """Inicializamos los atributos de la puntuación"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #Configuracion de fuente para la información de la puntuación
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        #Prepara la imagen de la puntuación inicial
        self.prep_score()
        self.prep_high_score()
        self.prep_level()


    def prep_score(self):
        """Convierte la puntuación en una imagen"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #Muestra la puntuación en la parte superior derecha de la pantalla
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        """Convierte la puntuación más alta en una imagen"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        #centra la puntuación más alta en la parte superior de la pantalla
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def check_high_score(self):
        #Comprueba si hay una nueva puntuación mas alta
        if(self.stats.score > self.stats.high_score):
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def show_score(self):
        """Dibuja la puntuación en la pantalla"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)


    def prep_level(self):
        """Prepara el nivel en una imagen"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        #Coloca el nivel debajo de la puntuación
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom - 10




