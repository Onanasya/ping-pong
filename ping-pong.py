from pygame import *

win_width = 700
win_height = 500

class GameSptite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = speed

        self.rect = self.image.get.rect()
        self.rect.x = player_x
        self.rect.y = player_y

#класс для ракеток
class Racket():
    pass

#класс для мячика
class Ball():
    pass

#создание объектов классов
racket1 = Racket()
racket2 = Racket()
ball = Ball()

#создание окна
window = display.set_mode((win_width) (win_height))