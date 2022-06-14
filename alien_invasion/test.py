import sys
import pygame
from pygame.sprite import Sprite
from settings import Settings

class Stars:
    """Класс для создания звезд"""
    def __init__(self):
        """Создает ресурсы"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Stars")
        self.bg_color = (230, 230, 230)
        self.st = Stars(self)
        self.stars = pygame.sprite.Group()
        #self.st.starry_sky()

    def draw_stars(self):
        """Запуск основного цикла"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.stars.draw(self.screen)
            self.screen.fill(self.bg_color)
            self.st.blitme()
            self.st.starry_sky()

            self.stars.draw(self.screen)
            pygame.display.flip()

    def starry_sky(self):
        """Создает несколько рядов звезд"""
        stars = Stars(self)
        self.stars.add(stars)

    def blitme(self):
        """Рисует звезду в текушей позиции"""
        self.screen.blit(self.image, self.rect)

class Сelebrity(Sprite):
    """Класс для управления звездами"""
    def __init__(self, ai_game):
        """Выводит звезду и задает ее начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/img.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

if __name__ == '__main__':
    st = Stars()
    st.draw_stars()
    #sky = Stars()


 star_width, star_height = star.rect.size
        self.width = 800
        self.height = 1200
        self.x = self.width
        self.y = self.height
        star_width = randint(self.width, self.height)
        star_height = randint(self.width, self.height)
        self.stars.add(star)


screen_rect = self.screen.get_rect()
        for bullet in self.bullets.sprites():
            if bullet.rect.right >= 500:#screen_rect.right:
                self.stats.ships_left -= 1
                if self.stats.ships_left > 0:
                    #self.stats.ships_left -= 1
                    self.bullets.empty()
                    #self.target.empty()
                    #self.target.draw_target()
                    self.ship.center_ship()
                    sleep(0.5)
            else:
                self.stats.game_active = False

