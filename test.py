import pygame as pg
import sys

pg.init()

def kvadratas(color):
    for i in range(len(akv_list)):
        pg.draw.rect(screen, color, akv_list[i])

        collision = akv_list[i].collidelistall(akv_list)
        if i in collision:
            collision.remove(i)

        for x in collision:
            if akv_list[i][0] > akv_list[x][0]:
                akv_list[x][0] -= 10
            elif akv_list[i][0] < akv_list[x][0]:
                akv_list[x][0] += 10

            if akv_list[i][1] > akv_list[x][1]:
                akv_list[x][1] -= 10
            elif akv_list[i][1] < akv_list[x][1]:
                akv_list[x][1] += 10


switch = False
def judejimas_test():
    global switch

    if akv_list[0][0] > 500:
        akv_list[0][1] += 15
        switch = True
    elif akv_list[0][0] < 100:
        akv_list[0][1] += 15
        switch = False
    if switch == False:
        akv_list[0][0] += 10
    elif switch == True:
        akv_list[0][0] -= 10



def game():
    kvadratas(green)
    judejimas_test()



green = (0, 255, 0)
red = (255, 0, 0)
akv_list = []
bkv_list = []

for i in range(8):
    akv_list.append(pg.Rect(200, 100 + (i * 50), 30, 30))

for i in range(2):
    bkv_list.append(pg.Rect(400, 100 + (i * 20), 30, 30))


width, height = 800, 600

clock = pg.time.Clock()

screen = pg.display.set_mode((width, height))
pg.display.set_caption("testy")
def_font = pg.font.get_default_font()
font = pg.font.Font(def_font, 10)
font2 = pg.font.Font(def_font, 30)

pause = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONUP:
            pause = not pause

    clock.tick(20)

    if not pause:
        screen.fill((255, 255, 255))
        game()

    pg.display.flip()