import sys
import pygame
from pygame.sprite import Sprite

class Stars:
    """"Класс для создания звезд"""
    def __init__(self):
        """Создает ресурсы"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Stars")
        self.bg_color = (230, 230, 230)
        self.stars = pygame.sprite.Group()
        self._starry_sky()

    def draw_stars(self):
        """Запуск основного цикла"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self._update_screen()

    def _starry_sky(self):
        """Создание ряда звезд"""
        star = Celebrity(self)
        star_width, star_height = star.rect.size
        available_space_x = 1300 - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        #stars_height = self.stars.rect.height
        available_space_y = (1000 - (3 * star_height))
        number_rows = available_space_y // (2 * star_height)

        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Создание звезды и размещение его в ряду"""
        star = Celebrity(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.stars.draw(self.screen)
        pygame.display.flip()

class Celebrity(Sprite):
    """Класс, представляющий одну звезду"""
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