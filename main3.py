import pygame as pg
import sys
import random

pg.init()


def kvadratas1(pos_x, pos_y, rect_size):
    pg.draw.rect(screen, (255, 0, 0), (pos_x, pos_y, rect_size, rect_size))

def kvadratas2(pos_x, pos_y, rect_size):
    pg.draw.rect(screen, (0, 255, 0), (pos_x, pos_y, rect_size, rect_size))

clock = pg.time.Clock()

width, height = 800, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("testy")
def_font = pg.font.get_default_font()
font = pg.font.Font(def_font, 10)

kv1_posx = 50
kv2_posx = 600

kv1_hp = 100
kv2_hp = 100

roll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
death = False
endgame = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    clock.tick(5)
    screen.fill((255, 255, 255))

    kvadratas1(kv1_posx,50,30)
    kvadratas2(kv2_posx,50,30)
    text1 = font.render(str(kv1_hp), True, (0, 0, 0))
    text2 = font.render(str(kv2_hp), True, (0, 0, 0))
    screen.blit(text1, (kv1_posx + 5, 60))
    screen.blit(text2, (kv2_posx + 5, 60))



    if (kv1_posx + 30) < kv2_posx:
        kv1_posx += 10
        kv2_posx -= 10
    elif death == False:
        if kv1_hp >= 1 and kv2_hp >= 1:
            roll1 = random.choice(roll)
            kv1_hp -= roll1
            roll2 = random.choice(roll)
            kv2_hp -= roll2
    if death == False:
        if (kv1_hp < 1 or kv2_hp < 1):
            death = True
    if endgame == False:
        print(kv1_hp, kv2_hp)
        if (kv1_hp < 0 or kv2_hp < 0):
            if kv1_hp > kv2_hp:
                kv1_hp = str(kv1_hp) + "win"
                kv2_hp = str(kv2_hp) + "loss"
                endgame = True
            else:
                kv1_hp = str(kv1_hp) + "loss"
                kv2_hp = str(kv2_hp) + "win"
                endgame = True




    pg.display.flip()

