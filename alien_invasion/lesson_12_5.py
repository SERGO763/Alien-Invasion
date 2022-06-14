import sys

import pygame

class Keys:
    """Открывает пустое окно и фиксирует нажатие клавиш"""
    def __init__(self):
        """Открывает пустое окно"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Keys')
        self.bg_color = (230, 230, 230)

    def starting_the_cycle(self):
        """Запуск цикла"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self(event.type)
                elif event.type == pygame.KEYUP:
                    self(event.type)
                elif event.type == pygame.KEYDOWN:
                    self(event.type)
                elif event.type == pygame.KEYUP:
                    self(event.type)


if __name__ == '__main__':
    a = Keys()
    a.starting_the_cycle()
