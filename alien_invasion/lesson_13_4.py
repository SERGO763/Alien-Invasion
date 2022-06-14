import sys
import pygame
from pygame.sprite import Sprite
from random import randint

class RainDrop:
    """Класс создающий сетку из капель"""
    def __init__(self):
        """Создает ресурсы"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Rain Drop")
        self.bg_color = (230, 230, 230)
        self.drop_speed = 1.0
        self.drops = pygame.sprite.Group()
        self._make_it_rain()


    def drop(self):
        """Основной цикл"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            self.screen.fill(self.bg_color)
            self._update_screen()
            self._update_drops()
            self._mfvkl()

    def _update_screen(self):
        """Обновляет изображение на экране и отбражает новый экран."""
        self.drops.draw(self.screen)
        pygame.display.flip()

    def _make_it_rain(self):
        """Создание сетки из капель"""
        drop = Rain(self)
        drop_width, drop_height = drop.rect.size
        available_space_x = 1300 - (2 * drop_width)
        available_space_y = (1000 - (3 * drop_height))
        number_rows = available_space_y // (2 * drop_height)
        number_drop_x = available_space_x // (2 * drop_width)
        for row_number in range(number_rows):
            for drop_number in range(number_drop_x):
                self._create_drop(drop_number, row_number)

    def _create_drop(self, drop_number, row_number):
        """Создание капли и размещение ее в ряду"""
        drop = Rain(self)
        drop_width, drop_height = drop.rect.size
        a = randint(0, 70)
        drop.x = drop_width + 2 * drop_width * drop_number + a
        drop.rect.x = drop.x
        drop.rect.y = drop.rect.height + 2 * drop.rect.height * row_number + a
        #drop.rect.y = drop.rect.height
        self.drops.add(drop)

    def _update_drops(self):
        """Обновляет позиции всех капель в ряду"""
        #self.drops.update()
        #self._check_fleet_edges()

    def _check_fleet_edges(self):
        """Проверяет на достижение края экрана """
        for drop in self.drops.sprites():
            self._mfvkl()
            #if drop.check_edges():
            self._mfvkl()
            break

    def _mfvkl(self):
        """Снижает сетку на заданную величину"""
        screen_rect = self.screen.get_rect()
        for drop in self.drops.sprites():
            drop.rect.y += self.drop_speed
            if drop.rect.y >= screen_rect.height:
                drop.rect.y = -30


class Rain(Sprite):
    """Класс представляющий одну каплю"""
    def __init__(self, ai_game):
        """Инициализирует одну каплю и задает ее начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.drop = ai_game.drop
        self.image = pygame.image.load('images/img_4.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def check_edges(self):
        """Возвращает True, если капля находится снизу экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.height <= screen_rect.height:
            return True

    def update(self):
        """Перемещает каплю снизу вверх"""
        drop_speed = 1.0
        fleet_direction = -1
        self.y += drop_speed #* fleet_direction
        self.rect.y = self.y


if __name__ == '__main__':
    rd = RainDrop()
    rd.drop()