import sys

import pygame

from settings import Settings
from game_character import GameCharacter

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
           (self.settings.screen_width, self.settings.screen_height))

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Darth Vader")
        self.character = GameCharacter(self)

        # Назначение цвета фона.
        self.bg_color = (230, 230, 230)


    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self._update_screen()
        # При каждом проходе цикла перерисовывается экран.

    def _check_events(self):
        """Обрабатывает нажатия клпвиш и события мыши ."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # При каждом проходе цикла перерисовывается экран.


            # Отображение последнего прорисованного экрана.

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.character.blitme()
        pygame.display.flip()


if __name__=='__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()