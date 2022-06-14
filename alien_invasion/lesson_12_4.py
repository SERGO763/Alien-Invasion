import sys

import pygame

from settings import Settings
from lesson_ship_12_4 import Ship

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
           (self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((1200, 800))

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self .settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Назначение цвета фона.
        self.bg_color = (230, 230, 230)


    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
        # При каждом проходе цикла перерисовывается экран.

    def _check_events(self):
        """Обрабатывает нажатия клпвиш и события мыши ."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
            # Переместить корабль вправо.
            self.ship.rect.x += 1
            self.ship.rect.y += 1

            # При каждом проходе цикла перерисовывается экран.


            # Отображение последнего прорисованного экрана.

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__=='__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()