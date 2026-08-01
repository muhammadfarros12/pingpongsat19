from pygame import *

width = 700
height = 500

window = display.set_mode((width, height))

background_color = (25, 184, 209)

window.fill(background_color)

game = True
FPS = 60
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    display.update()
    clock.tick(FPS)
    

