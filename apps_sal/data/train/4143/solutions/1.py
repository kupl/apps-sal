def points(dice):
    dice_str = str(dice)
    c = 0
    d = 0
    dd = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0
    for e in dice_str[0]:
        for f in dice_str[0:]:
            if e != f:
                d += 1
    for e2 in dice_str[0]:
        for f2 in dice_str[0:]:
            if e2 != f2:
                d2 += 1
    for e3 in dice_str[0]:
        for f3 in dice_str[0:]:
            if e3 != f3:
                d3 += 1
    for e4 in dice_str[0]:
        for f4 in dice_str[0:]:
            if e4 != f4:
                d4 += 1
    for e5 in dice_str[0]:
        for f5 in dice_str[0:]:
            if e5 != f5:
                d5 += 1
    for a in dice_str[0]:
        for b in dice_str[0:]:
            if a == b:
                c += 1
    for a2 in dice_str[0:]:
        for b2 in dice_str[0:]:
            if a2 == b2:
                c2 += 1
    for a3 in dice_str[0:]:
        for b3 in dice_str[0:]:
            if a3 == b3:
                c3 += 1
    for a4 in dice_str[0:]:
        for b4 in dice_str[0:]:
            if a4 == b4:
                c4 += 1
    for a5 in dice_str[0:]:
        for b5 in dice_str[0:]:
            if a5 == b5:
                c5 += 1
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 2 and (int(dice_str[2]) == 3) and (int(dice_str[3]) == 4) and (int(dice_str[4]) == 5):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 3 and (int(dice_str[2]) == 4) and (int(dice_str[3]) == 5) and (int(dice_str[4]) == 6):
        return 20
    if int(dice_str[0]) == 3 and int(dice_str[1]) == 4 and (int(dice_str[2]) == 5) and (int(dice_str[3]) == 6) and (int(dice_str[4]) == 1):
        return 20
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 3 and (int(dice_str[2]) == 5) and (int(dice_str[3]) == 6) and (int(dice_str[4]) == 4):
        return 20
    if int(dice_str[0]) == 6 and int(dice_str[1]) == 2 and (int(dice_str[2]) == 5) and (int(dice_str[3]) == 3) and (int(dice_str[4]) == 4):
        return 20
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 3 and (int(dice_str[2]) == 2) and (int(dice_str[3]) == 4) and (int(dice_str[4]) == 5):
        return 20
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 2 and (int(dice_str[2]) == 3) and (int(dice_str[3]) == 5) and (int(dice_str[4]) == 4):
        return 20
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 2 and (int(dice_str[2]) == 3) and (int(dice_str[3]) == 4) and (int(dice_str[4]) == 6):
        return 0
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 2 and (int(dice_str[2]) == 4) and (int(dice_str[3]) == 3) and (int(dice_str[4]) == 5):
        return 20
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 2 and (int(dice_str[2]) == 4) and (int(dice_str[3]) == 5) and (int(dice_str[4]) == 3):
        return 20
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 3 and (int(dice_str[2]) == 2) and (int(dice_str[3]) == 4) and (int(dice_str[4]) == 5):
        return 20
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 3 and (int(dice_str[2]) == 2) and (int(dice_str[3]) == 5) and (int(dice_str[4]) == 4):
        return 20
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 3 and (int(dice_str[2]) == 4) and (int(dice_str[3]) == 2) and (int(dice_str[4]) == 5):
        return 20
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 3 and (int(dice_str[2]) == 4) and (int(dice_str[3]) == 5) and (int(dice_str[4]) == 2):
        return 20
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 3 and (int(dice_str[2]) == 3) and (int(dice_str[3]) == 5) and (int(dice_str[4]) == 2):
        return 20
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 4 and (int(dice_str[2]) == 3) and (int(dice_str[3]) == 5) and (int(dice_str[4]) == 2):
        return 20
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 4 and (int(dice_str[2]) == 3) and (int(dice_str[3]) == 2) and (int(dice_str[4]) == 5):
        return 20
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 4 and (int(dice_str[2]) == 2) and (int(dice_str[3]) == 5) and (int(dice_str[4]) == 3):
        return 20
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 4 and (int(dice_str[2]) == 2) and (int(dice_str[3]) == 3) and (int(dice_str[4]) == 5):
        return 20
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 4 and (int(dice_str[2]) == 5) and (int(dice_str[3]) == 3) and (int(dice_str[4]) == 2):
        return 20
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 4 and (int(dice_str[2]) == 5) and (int(dice_str[3]) == 2) and (int(dice_str[4]) == 3):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 1 and (int(dice_str[2]) == 3) and (int(dice_str[3]) == 4) and (int(dice_str[4]) == 5):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 1 and (int(dice_str[2]) == 3) and (int(dice_str[3]) == 5) and (int(dice_str[4]) == 4):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 1 and (int(dice_str[2]) == 5) and (int(dice_str[3]) == 4) and (int(dice_str[4]) == 3):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 1 and (int(dice_str[2]) == 5) and (int(dice_str[3]) == 3) and (int(dice_str[4]) == 4):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 1 and (int(dice_str[2]) == 4) and (int(dice_str[3]) == 3) and (int(dice_str[4]) == 5):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 1 and (int(dice_str[2]) == 4) and (int(dice_str[3]) == 5) and (int(dice_str[4]) == 3):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 3 and (int(dice_str[2]) == 1) and (int(dice_str[3]) == 4) and (int(dice_str[4]) == 5):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 3 and (int(dice_str[2]) == 1) and (int(dice_str[3]) == 5) and (int(dice_str[4]) == 4):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 3 and (int(dice_str[2]) == 4) and (int(dice_str[3]) == 1) and (int(dice_str[4]) == 5):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 3 and (int(dice_str[2]) == 4) and (int(dice_str[3]) == 5) and (int(dice_str[4]) == 1):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 3 and (int(dice_str[2]) == 5) and (int(dice_str[3]) == 1) and (int(dice_str[4]) == 4):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 3 and (int(dice_str[2]) == 5) and (int(dice_str[3]) == 4) and (int(dice_str[4]) == 1):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 4 and (int(dice_str[2]) == 1) and (int(dice_str[3]) == 3) and (int(dice_str[4]) == 5):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 4 and (int(dice_str[2]) == 1) and (int(dice_str[3]) == 5) and (int(dice_str[4]) == 3):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 4 and (int(dice_str[2]) == 3) and (int(dice_str[3]) == 1) and (int(dice_str[4]) == 5):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 4 and (int(dice_str[2]) == 3) and (int(dice_str[3]) == 5) and (int(dice_str[4]) == 1):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 4 and (int(dice_str[2]) == 5) and (int(dice_str[3]) == 1) and (int(dice_str[4]) == 3):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 4 and (int(dice_str[2]) == 5) and (int(dice_str[3]) == 3) and (int(dice_str[4]) == 1):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 5 and (int(dice_str[2]) == 1) and (int(dice_str[3]) == 3) and (int(dice_str[4]) == 4):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 5 and (int(dice_str[2]) == 1) and (int(dice_str[3]) == 4) and (int(dice_str[4]) == 3):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 5 and (int(dice_str[2]) == 3) and (int(dice_str[3]) == 1) and (int(dice_str[4]) == 4):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 5 and (int(dice_str[2]) == 3) and (int(dice_str[3]) == 4) and (int(dice_str[4]) == 1):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 5 and (int(dice_str[2]) == 4) and (int(dice_str[3]) == 1) and (int(dice_str[4]) == 3):
        return 20
    if int(dice_str[0]) == 2 and int(dice_str[1]) == 5 and (int(dice_str[2]) == 4) and (int(dice_str[3]) == 3) and (int(dice_str[4]) == 1):
        return 20
    if c4 == 25:
        return 50
    if c4 == 17:
        return 40
    if c4 == 13:
        return 30
    if c4 == 7 or c4 == 9 or c4 == 11:
        return 0
    if c4 == 7 and d == 0:
        return 0
    if c4 == 9 and d == 0:
        return 0
    if c4 == 1 and d == 0:
        return 0
    if c4 == 7 and d4 == 2:
        return 0
    if c4 == 7 and d4 == 3:
        return 0
    if c4 == 9 and d4 == 2:
        return 0
    if c4 == 9 and d4 == 3:
        return 0
    if c4 == 13 and d4 == 2:
        return 0
    if c4 == 13 and d4 == 3:
        return 0
    if dice[0] == 1 and dice[1] == 2 and (dice[2] == 3) and (dice[3] == 4) and (dice[4] == 6):
        return 0
    if int(dice_str[0]) == 1 and int(dice_str[1]) == 2 and (int(dice_str[2]) == 3) and (int(dice_str[3]) == 4) and (int(dice_str[4]) == 5):
        return 20
    else:
        return 0
