from pygame import *

win_width = 700
win_height = 500

class GameSptite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

#класс для ракеток
class Racket(GameSptite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        bulet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 15)
        bulets.add(bulet)

#класс для мячика
class Ball():
    pass

#создание объектов классов
racket1 = Racket('asteroid.png', 5, 100, 10, 100, 15)
#racket2 = Racket()
ball = Ball()
game = True

#создание окна
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')
back_ground = transform.scale(image.load('fon.jpg'), (win_width, win_height))

#цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(back_ground, (0, 0))
    racket1.update()

    display.update()
time.delay(50)
