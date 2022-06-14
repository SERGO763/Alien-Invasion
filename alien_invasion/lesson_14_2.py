import sys
import pygame
from pygame.sprite import Sprite
from time import sleep
import pygame.font

class TargetShooting:
    """Класс для управления ресурсами и поведением игры"""
    def __init__(self):
        """Инициализирует игруи создает игровые ресурсы"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption('Target Shooting')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.target = Target(self)
        self.stats = GameStats(self)
        self.bullet = Bullet(self)
        self.play_button = Button(self, 'Play')
        self.settings = Settings(self)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                self._update_target()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play"""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.bullets.empty()
            self.ship.center_ship()

    def _check_keydown_events(self, event):
        """Реагирует на нажатия клавиш"""
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

    def _check_fleet_edges(self):
        """Реагирует на достижение мишени края экрана"""
        if self.target.check_edges():
            self.target.fleet_direction *= -1


    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и удаляет старые снаряды"""
        self.bullets.update()
        #for bullet in self.bullets.copy():
            #if bullet.rect.right >= 1600:
                #self.bullets.remove(bullet)
            #print(len(self.bullets))
        collisions = pygame.sprite.spritecollideany(self.target, self.bullets)
        self._ship_hit()
        #self.settings.increase_speed()
        self.settings.target_speed_factor *= self.settings.speedup_scale

    def _update_target(self):
        """Обновляет позиции мишени"""
        self.target.update()
        self.target.draw_target()
        self.target.check_edges()
        self._check_fleet_edges()

    def _update_screen(self):
        """ОБновляет изображения на экране и отображает новый экран"""
        pygame.display.flip()
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        if not self.stats.game_active:
            self.play_button.draw_button()

    def _ship_hit(self):
        """Обрабатывает промахи пули с мишенью"""
        #self.bullets.update()
        if self.stats.ships_left > 0:
            for bullet in self.bullets.sprites():
                if bullet.rect.right >= 1200:
                    self.stats.ships_left -= 1
                    self.settings.initialize_dynamic_settings()
                    self.bullets.empty()
                    self.ship.center_ship()
                    sleep(0.5)
        else:
            self.stats.game_active = False

class Settings():
    def __init__(self, ai_game):
        self.speedup_scale = 0.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.target_speed_factor = 1.1
        self.bullet_speed_factor = 3.0
        #self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости игры"""
        self.target_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale


class Ship():
    """Класс для управления кораблем"""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/img_7.png')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.ship_speed = 1.5
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.moving_up and self.rect.y > self.screen_rect.y:
            self.y -= self.ship_speed
        if self.moving_down and self.rect.y < 750:
            self.y += self.ship_speed

        self.rect.y = self.y

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль по середине левого края"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными кораблем"""
    def __init__(self, ai_game):
        """Создает объект снарядов в текущей позиции корабля"""
        super().__init__()
        self.screen = ai_game.screen
        self.bullet_speed = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.color = self.bullet_color

        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.x = float(self.rect.x)

    def update(self):
        """Перемещает снаряд вправо по экрану"""
        self.x += self.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Вывод снаряда на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)

class Target(Sprite):
    """Класс для управления мишенью"""
    def __init__(self, ai_game):
        """Создает мишень вправом углу экрана"""
        super().__init__()
        self.screen = ai_game.screen
        #self.target_speed = 1.25
        self.target_width = 50
        self.target_height = 100
        self.target_color = (60, 60, 60)
        self.color = self.target_color
        self.settings = Settings(self)
        self.fleet_direction = 1

        self.rect = pygame.Rect(1150, 0, self.target_width, self.target_height)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Перемещает мишень по экрану"""
        screen_rect = self.screen.get_rect()
        if self.rect.y >= screen_rect.height or self.rect.y <= 0:
            return True

    def update(self):
        """Перемещает мишень по экрану"""
        self.y += (self.settings.target_speed_factor * self.fleet_direction)
        self.rect.y = self.y

    def draw_target(self):
        """Вывод мишени на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)

class GameStats():
    """Отслеживание статистики для игры"""
    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.ship_limit = 8
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Инициализирует статистику изменяющуюся в ходе игры"""
        self.ships_left = self.ship_limit

class Button():
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height = 200, 50
        self.botton_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру """
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.botton_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Отображение пустой кнопки и вывод сообщения"""
        self.screen.fill(self.botton_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

if __name__ == '__main__':
    ts = TargetShooting()
    ts.run_game()