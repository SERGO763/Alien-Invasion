import sys
import pygame
from pygame.sprite import Sprite
from random import randint

class Stars:
    """Класс для создания звезд"""
    def __init__(self):
        """Создает ресурсы"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Stars")
        self.bg_color = (230, 230, 230)
        self.stars = pygame.sprite.Group()
        self._starry_sky()
        #self._random_star()

    def draw_stars(self):
        """Запуск основного цикла"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self._update_screen()
            #self._random_star()

    def _starry_sky(self):
        """Создает ряд звезд"""
        star = Celebrity(self)
        star_width, star_height = star.rect.size
        available_space_x = 1300 - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_height)
        available_space_y = (1000 - (3 * star_height))
        number_rows = available_space_y // (2 * star_height)

        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _random_star(self):
        """Отклоняет звезду"""
        star = Celebrity(self)
        #star_width = 800
        #star_height = 1200
        star_width = randint(0, 100)
        self.stars.add(star)
        #self.stars.add(self.star_width)

    def _create_star(self, star_number, row_number):
        """Создание звезды и размещние ее в ряду"""
        star = Celebrity(self)
        star_width, star.height = star.rect.size
        a = randint(0, 80)
        star.x = star_width + 2 * star_width * star_number + a
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number + a
        self.stars.add(star)

    def _update_screen(self):
        """Обновляет изображение на экране и отбражает новый экран."""
        self.stars.draw(self.screen)
        #self.stars.draw(star_width)
        pygame.display.flip()

class Celebrity(Sprite):
    """Класс представляющий одну звезду"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/img_2.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

if __name__ == '__main__':
    st = Stars()
    st.draw_stars()