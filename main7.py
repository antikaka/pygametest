
import pygame as pg
import sys
import random

pg.init()
def judejimas():

    kasgyvas()
    dist_check_a = 20
    for num, a in enumerate(akv_list):
        if num in lavonai_a or len(lavonai_b) == len(bkv_list):
            continue
        min_diff = 1000
        for num2, b in enumerate(bkv_list):
            if num2 in lavonai_b:
                continue
            check_x = a[0] - b[0]
            check_y = a[1] - b[1]
            total_diff = abs(check_x) + abs(check_y)
            if min_diff > total_diff:
                min_diff = total_diff
                check_x_min = check_x
                check_y_min = check_y
        if min_diff > dist_check_a:
            if check_x_min > dist_check_a and check_y_min > dist_check_a:
                a[0] -= 5
                a[1] -= 5
            elif check_x_min < -dist_check_a and check_y_min < -dist_check_a:
                a[0] += 5
                a[1] += 5
            elif check_x_min > dist_check_a:
                a[0] -= 10
            elif check_x_min < -dist_check_a:
                a[0] += 10
            elif check_y_min > dist_check_a:
                a[1] -= 10
            elif check_y_min < dist_check_a:
                a[1] += 10
    dist_check_b = 20
    for num, b in enumerate(bkv_list):
        if num in lavonai_b or len(lavonai_a) == len(akv_list):
            continue
        min_diff = 1000
        for num2, a in enumerate(akv_list):
            if num2 in lavonai_a:
                continue
            check_x = b[0] - a[0]
            check_y = b[1] - a[1]
            total_diff = abs(check_x) + abs(check_y)
            if min_diff > total_diff:
                min_diff = total_diff
                check_x_min = check_x
                check_y_min = check_y
        if min_diff > dist_check_b:
            if check_x_min > dist_check_b and check_y_min > dist_check_b:
                b[0] -= 5
                b[1] -= 5
            elif check_x_min < -dist_check_b and check_y_min < -dist_check_b:
                b[0] += 5
                b[1] += 5
            elif check_x_min > dist_check_b:
                b[0] -= 10
            elif check_x_min < -dist_check_b:
                b[0] += 10
            elif check_y_min > dist_check_b:
                b[1] -= 10
            elif check_y_min < dist_check_b:
                b[1] += 10

    for num, b in enumerate(bkv_list):
        if num not in lavonai_b:
            collision = b.collidelistall(bkv_list)
            if b in collision:
                collision.remove(b)
            for x in collision:
                if b[0] > bkv_list[x][0]:
                    b[0] += 10
                    bkv_list[x][0] -= 10
                if b[0] < bkv_list[x][0]:
                    b[0] -= 10
                    bkv_list[x][0] += 10
                if b[1] > bkv_list[x][1]:
                    b[1] += 10
                    bkv_list[x][1] -= 10
                if b[1] < bkv_list[x][1]:
                    b[1] -= 10
                    bkv_list[x][1] += 10

    for num, b in enumerate(akv_list):
        if num not in lavonai_a:
            collision = b.collidelistall(akv_list)
            if b in collision:
                collision.remove(b)
            for x in collision:
                if b[0] > akv_list[x][0]:
                    b[0] += 10
                    akv_list[x][0] -= 10
                if b[0] < akv_list[x][0]:
                    b[0] -= 10
                    akv_list[x][0] += 10
                if b[1] > akv_list[x][1]:
                    b[1] += 10
                    akv_list[x][1] -= 10
                if b[1] < akv_list[x][1]:
                    b[1] -= 10
                    akv_list[x][1] += 10

    damage_push = 5
    damage_roll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num, a in enumerate(akv_list):
        if num not in lavonai_a:
            collisionvs = a.collidelist(bkv_list)
            if collisionvs == -1:
                continue
            else:
                damage = random.choice(damage_roll)
                bkv_hp[collisionvs] -= damage
                if bkv_list[collisionvs][0] > akv_list[num][0]:
                    bkv_list[collisionvs][0] += damage_push
                elif bkv_list[collisionvs][0] < akv_list[num][0]:
                    bkv_list[collisionvs][0] -= damage_push

    for num, b in enumerate(bkv_list):
        if num not in lavonai_b:
            collisionvs = b.collidelist(akv_list)
            if collisionvs == -1:
                continue
            else:
                damage = random.choice(damage_roll)
                akv_hp[collisionvs] -= damage
                if akv_list[collisionvs][0] > bkv_list[num][0]:
                    akv_list[collisionvs][0] += damage_push
                elif akv_list[collisionvs][0] < bkv_list[num][0]:
                    akv_list[collisionvs][0] -= damage_push

lavonai_a = []
lavonai_b = []
def kasgyvas():
    for key, value in akv_hp.items():
        if value <= 0 and key not in lavonai_a:
            lavonai_a.append(key)


    for key, value in bkv_hp.items():
        if value <= 0 and key not in lavonai_b:
            lavonai_b.append(key)


def scoreboard():
    a_hp = 0
    b_hp = 0
    for value in akv_hp.values():
        if value < 0:
            continue
        else:
            a_hp += value

    for value in bkv_hp.values():
        if value < 0:
            continue
        else:
            b_hp += value
    # print(a_hp, b_hp)
    if a_hp < 0:
        a_hp = 1
    if b_hp < 0:
        b_hp = 1
    percentage = (a_hp / (a_hp + b_hp)) * 100
    size = (400 / 100) * percentage
    if size < 22 and size > 2:
        size = 20
    # print(percentage, size)
    pg.draw.rect(screen, red, (200,30, 400, 50))
    pg.draw.rect(screen, green, (200, 30, size, 50))
    pg.draw.rect(screen, (0, 0, 0), (200, 30, 400, 50), 1)



def playfield():
    pos_y = 100
    for i in range(10):
        pos_x = 200
        for i2 in range(12):
            pg.draw.rect(screen, (0,0,0), (pos_x, pos_y, 40, 40), 1)
            pos_x += 40
        pos_y += 40

demo = False
def demostate():
    pos_y = 105
    for i in range(10):
        rect_b = pg.Rect(645, pos_y, 30, 30)
        pg.draw.rect(screen, red, rect_b)
        pos_y += 40

    pos_y = 105
    for i in range(10):
        rect_a = pg.Rect(205, pos_y, 30, 30)
        pg.draw.rect(screen, green, rect_a)
        pos_y += 40


place_kv = []
akv_list = []

pick = pg.Rect(100, 400, 30, 30)
def gamestart():
    clock.tick(30)
    if gamestarted == False:
        global pick
        pos_y = 100
        for i in range(10):
            pos_x = 200
            for i2 in range(2):
                place = pg.Rect(pos_x, pos_y, 40, 40)
                pg.draw.rect(screen, red, place, 1)
                place_kv.append(place)
                pos_x += 40
            pos_y += 40



        pg.draw.rect(screen, green, pick)

        if event.type == pg.MOUSEBUTTONUP and pick.topleft != (100, 400):
            pick = pg.Rect(100, 400, 30, 30)
            pg.draw.rect(screen, green, pick)

        if demo == True:
            demostate()

        for x in akv_list:
            if x not in place_kv:
                akv_list.remove(x)
            else:
                pg.draw.rect(screen, green, (x[0] +5, x[1] + 5, 30, 30))




bkv_list = []



bkv_hp = {}


akv_hp = {}
def game():
    clock.tick(5)
    playfield()

    if demo == False and len(bkv_list) == 0:
        pos_y = 105
        for i in range(10):
            rect_b = pg.Rect(645, pos_y, 30, 30)
            bkv_list.append(rect_b)
            pos_y += 40

    if demo and len(bkv_list) == 0:
        pos_y = 105
        for i in range(10):
            rect_b = pg.Rect(645, pos_y, 30, 30)
            bkv_list.append(rect_b)
            pos_y += 40

        pos_y = 105
        for i in range(10):
            rect_a = pg.Rect(205, pos_y, 30, 30)
            akv_list.append(rect_a)
            pos_y += 40

    if len(bkv_hp) == 0:
        for num, x in enumerate(bkv_list):
            bkv_hp[num] = 100

    if len(akv_hp) == 0:
        for num, x in enumerate(akv_list):
            akv_hp[num] = 100
    for num, i in enumerate(bkv_list):
        if num not in lavonai_b:
            pg.draw.rect(screen, red, i)
            hp_text = font.render(str(bkv_hp[num]), True, (0, 0, 0))
            screen.blit(hp_text, (bkv_list[num][0] + 5, bkv_list[num][1] + 10))
        else:
            rip_text = bigfont.render("X", True, red)
            screen.blit(rip_text, (bkv_list[num][0], bkv_list[num][1]))

    for num, x in enumerate(akv_list):
        if num not in lavonai_a:
            pg.draw.rect(screen, green, (x[0] + 5, x[1] + 5, 30, 30))
            hp_text = font.render(str(akv_hp[num]), True, (0, 0, 0))
            screen.blit(hp_text, (akv_list[num][0] + 10, akv_list[num][1] + 15))
        else:
            rip_text = bigfont.render("X", True, green)
            screen.blit(rip_text, (akv_list[num][0], akv_list[num][1]))


    judejimas()
    scoreboard()

paused_list = []
def paused():
    if len(paused_list) != (len(bkv_list) + len(akv_list)):
        for x in akv_list:
            paused_list.append(x)
        for x in bkv_list:
            paused_list.append(x)
    for x in paused_list:
        pg.draw.rect(screen, (0, 0, 255), x, 1)

gamestarted = False

width, height = 800, 600

clock = pg.time.Clock()

screen = pg.display.set_mode((width, height))
pg.display.set_caption("testy")
def_font = pg.font.get_default_font()
font = pg.font.Font(def_font, 10)
font2 = pg.font.Font(def_font, 20)
bigfont = pg.font.Font(def_font, 30)

dragging = False
pause = False
red = (255, 0, 0)
green = (0, 255, 0)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONUP:
            mouse_pos = pg.mouse.get_pos()
            if start_mygtukas.collidepoint(mouse_pos) and gamestarted == False:
                gamestarted = True
            elif start_mygtukas.collidepoint(mouse_pos):
                pause = not pause
            elif demo_mygtukas.collidepoint(mouse_pos):
                demo = not demo


            if dragging:
                akv_list.append(pick)
                dragging = False
                collision = akv_list[-1].collidelistall(place_kv)
                if len(collision) > 0:
                    akv_list[-1] = place_kv[collision[0]]
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if pick.collidepoint(mouse_pos) and gamestarted == False:
                dragging = True

        elif event.type == pg.MOUSEMOTION:
            if dragging:
                pick.center = event.pos









    screen.fill((255, 255, 255))
    playfield()
    gamestart()

    if pause == True and gamestarted:
        screen.fill((255, 255, 255))
        playfield()
        paused()
        # print("paused")

    if pause == False and gamestarted:
        screen.fill((255, 255, 255))
        game()

    start_mygtukas = pg.Rect(20, 20, 150, 50)
    pg.draw.rect(screen, (255, 0, 0), start_mygtukas)
    pg.draw.rect(screen, (0, 0, 0), start_mygtukas, 1)
    pradzia_text = bigfont.render("START", True, (0, 0, 0))
    screen.blit(pradzia_text, (45, 30))

    if gamestarted == True:
        pg.draw.rect(screen, (0, 255, 0), start_mygtukas)
        pause_text = font2.render("Press here", True, (0, 0, 0))
        pause_text2 = font2.render(" for pause", True, (0, 0, 0))
        screen.blit(pause_text, (45, 25))
        screen.blit(pause_text2, (45, 40))

        if pause == True:
            pg.draw.rect(screen, (255, 255, 0), start_mygtukas)
            pause_text = font2.render("Press here", True, (0, 0, 0))
            pause_text2 = font2.render("to unpause", True, (0, 0, 0))
            screen.blit(pause_text, (45, 25))
            screen.blit(pause_text2, (45, 40))


    if gamestarted == False:
        demo_mygtukas = pg.Rect(690, 100, 100, 50)
        pg.draw.rect(screen, (255, 0, 0), demo_mygtukas)
        pg.draw.rect(screen, (0, 0, 0), demo_mygtukas, 1)
        demo_text = bigfont.render("DEMO", True, (0, 0, 0))
        screen.blit(demo_text, (695, 110))

    if demo == True and gamestarted == False:
        demo_mygtukas = pg.Rect(690, 100, 100, 50)
        pg.draw.rect(screen, (0, 255, 0), demo_mygtukas)
        pg.draw.rect(screen, (0, 0, 0), demo_mygtukas, 1)
        demo_text = bigfont.render("DEMO", True, (0, 0, 0))
        screen.blit(demo_text, (695, 110))



    pg.display.flip()