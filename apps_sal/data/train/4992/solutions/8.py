def bingo(card, numbers):
    card[3][2] = 'X'
    parsed_num = [int(x[1:len(x)]) for x in numbers]
    for n in parsed_num:
        card = [['X' if x == n else x for x in y] for y in card]
    if check_rows(card) or check_diag2(card) or check_diag1(card) or (check_columns(card) is True):
        return True
    else:
        return False


def check_columns(card):
    m = 0
    templist = []
    while m < 5:
        for k in range(1, 6):
            templist.append(card[k][m])
        if templist == ['X', 'X', 'X', 'X', 'X']:
            return True
        else:
            templist.clear()
            m += 1
            continue
    return False


def check_diag1(card):
    templist = []
    for i in range(1, 6):
        templist.append(card[i][i - 1])
    if templist == ['X', 'X', 'X', 'X', 'X']:
        return True
    else:
        return False


def check_diag2(card):
    templist = []
    for i in range(0, 5):
        templist.append(card[5 - i][i])
    if templist == ['X', 'X', 'X', 'X', 'X']:
        return True
    else:
        return False


def check_rows(card):
    for i in range(1, 6):
        if card[i] == ['X', 'X', 'X', 'X', 'X']:
            return True
        else:
            continue
    return False
