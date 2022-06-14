class GameStats():
    """Отслеживание статистики для игры Alien Invasion."""
    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()
        # Игра Alien Invasion запускается в неактивном состоянии.
        #self.game_active = True
        self.game_active = False
        # Рекорд не должен сбрасываться
        with open('record.txt') as file_object:
            self.high_score = file_object.read()
            self.high_score = int(self.high_score)

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def record(self):
        """Открывает фаил с рекордом"""
        with open('record.txt') as file_object:
            self.high_score = file_object.read()
