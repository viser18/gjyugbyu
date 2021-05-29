from pygame import *
from pygame import time
from random import randint
from time import time as timer
font.init()

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
            self.image = transform.scale(image.load("yes1.png"),(25,100))
        if keys[K_DOWN] and self.rect.y < 550:
            self.rect.y += self.speed
            self.image = transform.scale(image.load("yes11.png"),(25,100))
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
            self.image = transform.scale(image.load("yes2.png"),(25,100))
        if keys[K_s] and self.rect.y < 550:
            self.rect.y += self.speed
            self.image = transform.scale(image.load("yes22.png"),(25,100))
    
back = (200,100,250)

s1 = 0
s2 = 0
ss2 = 0
ss1 = 0
font = font.SysFont("Arial",40)
pl1w = font.render("1 игрок победил!",True,(randint(0,245),randint(0,245),randint(0,245)))
pl2w = font.render("2 игрок победил!",True,(randint(0,245),randint(0,245),randint(0,245)))


window = display.set_mode((600,600))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60
pl1 = Player("yes1.png",30,200,4,25,100)
pl2 = Player("yes2.png",520,200,4,25,100)
ball = Gamesprite("мячик.png",240,200,4,100,75)
x = 3
y = 3
cccc = 0
ccc = 0
cc = randint(1,2)
c = 0
if cc == 2:
    x *=-1
else :
    x *=1
last_time = timer()


score1 = font.render(str(s1),True,(2,4,5))
score2 = font.render(str(s2),True,(6,7,8))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False



    
    

    if finish != True:
        window.fill(back)
        ball.reset()
        pl1.update_l()
        pl2.update_r()
        pl1.reset()
        pl2.reset()
        ball.rect.x += x
        ball.rect.y += y


        now_time = timer()
        if now_time - last_time > 3:
            score1 = font.render(str(s1),True,(randint(0,255),randint(0,255),randint(0,255)))
            score2 = font.render(str(s2),True,(randint(0,255),randint(0,255),randint(0,255)))
            last_time = timer()

        window.blit(score1,(10,10))
        window.blit(score2,(570,10))
        
        if ball.rect.y >510 or ball.rect.y <-10:
            y *=-1
        
        if sprite.collide_rect(ball,pl1) or sprite.collide_rect(ball,pl2):
            x *= -1
            c += 1
        if c >= 3 and x > 0:
            x +=1
            c = 0
        if ball.rect.x < 30:
            ball.rect.x = 240
            ball.rect.y =200
            ccc += 1
            s2 += 1
            x = 3
        if ball.rect.x > 520:
            cccc += 1 
            s1 += 1
            ball.rect.x = 240
            ball.rect.y =200
            x = 3
        if ccc >3 :
            window.blit(pl1w,(240,200))
        if cccc >3 :
            window.blit(pl2w,(240,200))
    display.update()
    clock.tick(FPS)
