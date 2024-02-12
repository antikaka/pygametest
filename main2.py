import pygame as pg
import sys

pg.init()


def kvadratas1():
    ...

width, height = 800, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("testy")
def_font = pg.font.get_default_font()
font = pg.font.Font(def_font, 30)



rect_size = 30
quant = 1
pos = [30, 90, 150, 210, 270]
pos_x = 50

test = "1 2 3 4 5".split()





while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    for num in range(quant):
        rect_dist = 0
        rect_dist += 30
        pos_y = pos[num] + rect_dist
        pg.draw.rect(screen, (255, 0, 0), (pos_x, pos_y, rect_size, rect_size))
        pg.draw.rect(screen, (0, 255, 0), (pos_x + 650, pos_y, rect_size, rect_size))
        text = font.render(test[num], True, (0, 0, 0))
        screen.blit(text, (pos_x, pos_y))




    pg.display.flip()













































