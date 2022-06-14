import pygame

class GameCharacter():
    """Класс который рисует персонажа"""
    def __init__(self, ai_game):
        """Инициализирует персонажа и задает его начальное положение"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение персонажа и получает прямоугольник.
        self.image = pygame.image.load('images/character.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый персонаж появляется в середине экрана.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Рисует персонажа в текущей позиции"""
        self.screen.blit(self.image, self.rect)

