import sys
import pygame
from pygame.sprite import Sprite


class SideShooting:
    """Класс для управления ресурсами и поведением игры"""
    def __init__(self):
        """Инициализирует игру и задает игровые ресурсы"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Side Shooting")
        self.bg_color = (230, 230, 230)
        self.ship = Ship(self)
        self.alien = Alien(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        #self.alien = Alien(self)
        #self.fleet_direction = 1

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self.bullets.update()
            self._update_aliens()
            self._update_bullets()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Создание флота вторжения"""
        alien = Alien(self)
        alien_height, alien_width = alien.rect.size
        available_space_y = 900 - (2 * alien_height)
        number_aliens_y = available_space_y // (2 * alien_height)

        ship_width = self.ship.rect.width
        available_space_x = (1000 - (3 * alien_width) - ship_width)
        number_rows = available_space_x // (2 * alien_width)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_y):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Создание пришельца и размещение его в ряду"""
        alien = Alien(self)
        alien_height, alien_width = alien.rect.size
        alien.y = alien_height + 2 * alien_height * alien_number
        alien.rect.y = alien.y
        alien.rect.x = alien.rect.width + 2 * alien.rect.width * row_number + 500
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота"""
        for alien in self.aliens.sprites():
            alien.fleet_direction *= -1
            alien.rect.x -= self.alien.fleet_drop_speed

    def _update_bullets(self):
        """Обновляет позиции сна рядов и унич тожает старые снаряды"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.right >= 1600:
                self.bullets.remove(bullet)
            #print(len(self.bullets))
            collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран"""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев во флоте"""
        self._check_fleet_edges()
        self.aliens.update()

class Ship():
    """Класс для управления кораблем"""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/img_7.png')
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.screen_rect.bottomleft
        self.ship_speed = 1

        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позициию корабля с учетом флага"""
        if self.moving_up and self.rect.y > self.screen_rect.y:
            self.y -= self.ship_speed
        if self.moving_down and self.rect.y < 750:
            self.y += self.ship_speed

        self.rect.y = self.y

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

class Bullet(Sprite):
    """Класс для управления снарядами, выпущенные кораблем"""
    def __init__(self, ai_game):
        """Создает обьект снарядов в текущей позиции корабля"""
        self.bullet_speed = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        super().__init__()
        self.screen = ai_game.screen

        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.x = float(self.rect.x)

    def update(self):
        """Перемещает снаряд вверх по экрану"""
        self.x += self.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Вывод снаряда на экран"""
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)

class Alien(Sprite):
    """Класс представляющий одного пришельца"""
    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load('images/alien_1.bmp')
        self.rect = self.image.get_rect()
        self.y = float(self.rect.y)
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.fleet_drop_speed = 10
        self.screen_rect = ai_game.screen.get_rect()

    def check_edges(self):
        """Возвращает True, если прищелец находится у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.y >= screen_rect.height or self.rect.y <= 0:
            return True

    def update(self):
        """Перемещает прищельца вниз или вверх"""
        self.y += (self.alien_speed * self.fleet_direction)
        self.rect.y = self.y

if __name__ == '__main__':
    ss = SideShooting()
    ss.run_game()