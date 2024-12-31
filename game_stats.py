class GameStats:
    """Gestiona las estadisticas de alien invaders"""


    def __init__(self, ai_game):
        """Inicializa las estadísticas"""
        self.settings = ai_game.settings
        self.reset_stats()

        # inicia alien invasion en estado activo
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ships_limit

