from sys import platlibdir
from turtle import window_height
from pygame import *

width = 700
height = 500

window = display.set_mode((width, height))

background_color = (25, 184, 209)

window.fill(background_color)

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #e.g. 55,55 - parameters
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 10:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - 10:
            self.rect.y += self.speed


player1 = Player('racket.png', 30, 200, 4, 50, 150)
player2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

game = True
FPS = 60
clock = time.Clock()

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.fill(background_color)

    player1.reset()
    player2.reset()
    ball.reset()

    player1.update_l()
    player2.update_r()

    # bola default bergerak secara diagonal
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    # ketika bola menyentuh dasar bawah/atas maka dipantulkan
    if ball.rect.y > height - 50 or ball.rect.y < 0:
        speed_y *= -1
    
    # ketika bolah menyentuh racket maka akan digerakan ke sebaliknya (mantul)
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
        speed_y *= -1

    
    display.update()
    clock.tick(FPS)
    

