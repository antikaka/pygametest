
import pygame as pg
import sys
import random

pg.init()

def playfield(pos_x, pos_y):
    pg.draw.rect(screen, (0,0,0), (pos_x, pos_y, 40, 40), 1)

def kvadratas(pos_x, pos_y, color, nr):
    pg.draw.rect(screen, color, (pos_x,pos_y, 30, 30))
    if color == green:
        text_hp_a = font.render(str(akv_hp[nr]), True, (0, 0, 0))
        screen.blit(text_hp_a, (pos_x + 5, pos_y + 10))
    if color == red:
        text_hp_b = font.render(str(bkv_hp[nr]), True, (0, 0, 0))
        screen.blit(text_hp_b, (pos_x + 5, pos_y + 10))

def kas_gyvas_a():
    gyvas_a = []
    for key, value in akv_hp.items():
        if value > 0:
            gyvas_a.append(key)

        if value < 0 and key in musasi_a:
            musasi_a.pop(key)

    return gyvas_a

def kas_gyvas_b():
    gyvas_b = []
    for key, value in bkv_hp.items():
        if value > 0:
            gyvas_b.append(key)

        if value < 0 and key in musasi_b:
            musasi_b.pop(key)


    return gyvas_b

musasi_a = {}
musasi_b = {}

def judejimas_a():
    gyvas_a = kas_gyvas_a()
    gyvas_b = kas_gyvas_b()
    if len(gyvas_b) == 0:
        return
    for a_kv in gyvas_a:
        min_diff = 1000
        for b_kv in gyvas_b:
            poscheck_0 = akv_pos[a_kv][0] - bkv_pos[b_kv][0] + 40
            poscheck_1 = akv_pos[a_kv][1] - bkv_pos[b_kv][1]
            pos_diff =  abs(poscheck_0) + abs(poscheck_1)
            # print(pos_diff)
            if pos_diff < min_diff:
                poscheck_0_min = poscheck_0
                poscheck_1_min = poscheck_1
                min_diff = pos_diff
                target = b_kv
        # print("akv", a_kv, "target", target)
        text_target = font.render(str(target), True, (0, 0, 0))
        screen.blit(text_target, (akv_pos[a_kv][0], akv_pos[a_kv][1]))
        if abs(poscheck_0_min) < 10 and abs(poscheck_1_min) < 10:
            musasi_a[a_kv] = target
            continue
        elif poscheck_0_min > 10:
            akv_pos[a_kv][0] -= 5
        elif poscheck_0_min < 10:
            akv_pos[a_kv][0] += 5
        elif poscheck_1_min > 10:
            akv_pos[a_kv][1] -= 5
        elif poscheck_1_min < 10:
            akv_pos[a_kv][1] += 5

def judejimas_b():
    gyvas_a = kas_gyvas_a()
    gyvas_b = kas_gyvas_b()
    if len(gyvas_a) == 0:
        return
    for b_kv in gyvas_b:
        min_diff = 1000
        for a_kv in gyvas_a:
            poscheck_0 = bkv_pos[b_kv][0] - akv_pos[a_kv][0] - 40
            poscheck_1 = bkv_pos[b_kv][1] - akv_pos[a_kv][1]
            pos_diff =  abs(poscheck_0) + abs(poscheck_1)
            # print(pos_diff)
            if pos_diff < min_diff:
                poscheck_0_min = poscheck_0
                poscheck_1_min = poscheck_1
                min_diff = pos_diff
                target = a_kv
        # print("akv", a_kv, "target", target)
        text_target = font.render(str(target), True, (0, 0, 0))
        screen.blit(text_target, (bkv_pos[b_kv][0], bkv_pos[b_kv][1]))

        if abs(poscheck_0_min) < 10 and abs(poscheck_1_min) < 10:
            musasi_b[b_kv] = target
            continue
        elif poscheck_0_min > 10:
            bkv_pos[b_kv][0] -= 5
        elif poscheck_0_min < 10:
            bkv_pos[b_kv][0] += 5
        elif poscheck_1_min > 10:
            bkv_pos[b_kv][1] -= 5
        elif poscheck_1_min < 10:
            bkv_pos[b_kv][1] += 5


def mustynes():
    dmg_roll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    coin = [1, 2]
    cointoss = random.choice(coin)
    # print("musasi a", musasi_a)
    # print("musasi b", musasi_b)
    if cointoss == 1:
        for key, value in musasi_a.items():
            damage = random.choice(dmg_roll)
            bkv_hp[value] -= damage

        for key, value in musasi_b.items():
            damage = random.choice(dmg_roll)
            akv_hp[value] -= damage

    elif cointoss == 2:
        for key, value in musasi_b.items():
            damage = random.choice(dmg_roll)
            akv_hp[value] -= damage

        for key, value in musasi_a.items():
            damage = random.choice(dmg_roll)
            bkv_hp[value] -= damage





width, height = 800, 600

clock = pg.time.Clock()

screen = pg.display.set_mode((width, height))
pg.display.set_caption("testy")
def_font = pg.font.get_default_font()
font = pg.font.Font(def_font, 10)

red = (255, 0, 0)
green = (0, 255, 0)

akv_hp = {
    0:100,
    1:100,
    2:100,
    3:100,
    4:100,
    5:100,
    6:100,
    7:100,
    8:100,
    9:100,
}
bkv_hp = {
    0:100,
    1:100,
    2:100,
    3:100,
    4:100,
    5:100,
    6:100,
    7:100,
    8:100,
    9:100,
}

akv_pos = {
    0: [205, 0],
    1: [205, 0],
    2: [205, 0],
    3: [205, 0],
    4: [205, 0],
    5: [205, 0],
    6: [205, 0],
    7: [205, 0],
    8: [205, 0],
    9: [205, 0],
}
bkv_pos = {
    0: [565, 0],
    1: [565, 0],
    2: [565, 0],
    3: [565, 0],
    4: [565, 0],
    5: [565, 0],
    6: [565, 0],
    7: [565, 0],
    8: [565, 0],
    9: [565, 0],
}
pos_y = 105
pos_x = 200
for i in akv_pos.keys():
    akv_pos[i][1] = pos_y
    pos_y += 40

pos_y = 105
for i in bkv_pos.keys():
    bkv_pos[i][1] = pos_y
    pos_y += 40



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


    screen.fill((255, 255, 255))
    clock.tick(5)

    pos_y = 100
    for i in range(10):
        pos_x = 200
        for i2 in range(10):
            playfield(pos_x, pos_y)
            pos_x += 40
        pos_y += 40

    for i in akv_pos.keys():
        kvadratas(akv_pos[i][0], akv_pos[i][1], green, i)

    for i in bkv_pos.keys():
        kvadratas(bkv_pos[i][0], bkv_pos[i][1], red, i)

    judejimas_a()
    judejimas_b()
    mustynes()

    pg.display.flip()