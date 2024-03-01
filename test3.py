
import pygame as pg
import sys
import random

pg.init()
boom_color = 100
boom_size = 5
boom_cords = (0, 0)
def explosion(coords):
    global boom_color, boom_size, boom
    if boom == True:
        boom_color += 30
        boom_size += 5
        pg.draw.circle(screen, (boom_color, 0, 0), (coords), boom_size)
    if boom_size == 25:
        boom = False
        boom_color = 100
        boom_size = 5


width, height = 800, 600

clock = pg.time.Clock()
screen = pg.display.set_mode((width, height))
pg.display.set_caption("kv TD")
def_font = pg.font.get_default_font()
font = pg.font.Font(def_font, 10)


brown = (220, 140, 70)
linija_s = (300, 300)
linija_e = [350, 350]
kv = pg.math.Vector2(25, 70)
kv_test = pg.Rect(25, 70, 30, 30)
dragging = False

kv2_test = pg.Rect(300, 300, 10, 10)
kv2 = pg.math.Vector2(kv2_test[0], kv2_test[1])

hp = 100
boom = False
shot_hit = False
while True:
    clock.tick(20)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONUP:
            # print("msbuttonup")
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

    screen.fill((255, 255, 255))
    # pg.draw.rect(screen, brown, (100, 100, 600, 400))
    pg.draw.circle(screen, (0, 0, 0), (300, 300), 50, 1)
    pg.draw.line(screen, (0, 0, 0), linija_s, (kv_test.center))
    pg.draw.rect(screen, (0, 255, 0), kv_test)
    pg.draw.rect(screen, (255, 0, 0), kv2_test)

    if kv2_test[0] == 300 and kv2_test[1] == 300:
        shoot_me = (kv_test.centerx - 5, kv_test.centery - 5)

    if shot_hit == False:
        kv2.move_towards_ip((shoot_me), 10)
        kv2_test[0], kv2_test[1] = kv2[0], kv2[1]
    collide_test = kv_test.colliderect(kv2_test)


    if collide_test == True or shoot_me == kv2:
        boom_cords = kv2
        kv2_test[0], kv2_test[1] = 300, 300
        kv2 = pg.math.Vector2(kv2_test[0], kv2_test[1])
        boom = True


    explosion(boom_cords)

    if collide_test == True:
        dmg = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        dmg_roll = random.choice(dmg)
        hp -= dmg_roll

    text = font.render(str(hp), 1, (0, 0, 0))
    screen.blit(text, (kv_test))
    print(kv2[0], kv2[1])







    # print(linija_e)

    pg.display.flip()