class GameStats:
    """Gestiona las estadisticas de alien invaders"""


    def __init__(self, ai_game):
        """Inicializa las estadísticas"""
        self.settings = ai_game.settings
        self.reset_stats()

        # inicia alien invasion en estado activo
        self.game_active = False

        # La puntuación más alta no debe restablecerse nunca
        self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.settings.ships_limit
        self.score = 0
        self.level = 1
