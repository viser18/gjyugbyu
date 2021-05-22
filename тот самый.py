from pygame import *
from pygame import time
from random import randint
from time import time as timer


class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y , player_speed,width = 50,heght=50):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,heght))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y)) 







class Player(Gamesprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
            self.player_image= "yes1.png"
        if keys[K_DOWN] and self.rect.y < 550:
            self.rect.y += self.speed
            self.player_image= "yes11.png"
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
            self.player_image= "yes2.png"
        if keys[K_s] and self.rect.y < 550:
            self.rect.y += self.speed
            self.player_image= "yes22.png"
    
back = (200,100,250)







window = display.set_mode((600,600))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 240

pl1 = Player("yes1.png",30,200,4,50,100)
pl2 = Player("yes2.png",520,200,4,50,100)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    

    if finish != True:
        window.fill(back)
        pl1.update_l()
        pl2.update_r()
        pl1.reset()
        pl2.reset()
    display.update()
    clock.tick(FPS)
