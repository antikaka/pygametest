
import pygame as pg
import sys

pg.init()


def krenta():
    for kv in kv_list:
        if kv[1] < 700:
            kv[1] += 1

        if dragging == False:
            collision = kv.collidelistall(coll_check)
            if len(collision) > 0:
                kv[1] -= 1





width, height = 800, 600

clock = pg.time.Clock()
screen = pg.display.set_mode((width, height))
pg.display.set_caption("collidey")
def_font = pg.font.get_default_font()

black = (0, 0, 0)
green = (0, 255, 0)

dragging = False

kv_test = pg.Rect(25, 70, 30, 30)
linija = pg.Rect(0, 498, 700, 1)
kibiras1 = pg.Rect(20, 70, 2, 30)
kibiras2 = pg.Rect(57, 70, 2, 30)
kibiras3 = pg.Rect(20, 100, 40, 1)

coll_check = linija, kibiras1, kibiras2, kibiras3

kv_list = []

while True:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONUP:
            # print("msbuttonup")
            kv_list.append(kv_test)
            if dragging:
                dragging = False


        if event.type == pg.MOUSEBUTTONDOWN:
            # print("msbuttndown")
            mouse_pos = pg.mouse.get_pos()
            if kv_test.collidepoint(mouse_pos):
                dragging = True

        elif event.type == pg.MOUSEMOTION:
            # print("msmotion")
            mouse_pos = pg.mouse.get_pos()
            if dragging:
                kv_test.center = mouse_pos


    clock.tick(50)

    screen.fill((255, 255, 255))



    pg.draw.line(screen, black, (20, 70), (20, 100), 5)
    pg.draw.line(screen, black, (60, 70), (60, 100), 5)
    pg.draw.line(screen, black, (20, 100), (60, 100), 5)
    pg.draw.line(screen, black, (0, 500), (700, 500), 5)

    if len(kv_list) < 1:
        pg.draw.rect(screen, green, kv_test)

    if len(kv_list) >= 1 and dragging == False:
        kv_test = pg.Rect(25, 70, 30, 30)

        pg.draw.rect(screen, green, kv_test)


    for kv in kv_list:
        pg.draw.rect(screen, green, kv)


    # pg.draw.rect(screen, green, kibiras3)
    # pg.draw.rect(screen, (255, 255, 255), linija)


    if dragging == False:
        krenta()


    pg.display.flip()
