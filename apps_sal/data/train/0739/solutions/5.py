def parse(movestr):
    moves = []
    acc = ''
    for char in movestr:
        char = char.upper()
        if char == 'R' or char == 'L':
            if acc != '':
                moves.append(int(acc))
            acc = ''
            moves.append(char)
        elif char.isdigit():
            acc += char
        elif len(acc) > 0:
            moves.append(int(acc))
            acc = ''
    if len(acc) > 0:
        moves.append(int(acc))
    return moves


def make_move(x, y, direc, dist):
    if direc == 0:
        y += dist
    elif direc == 1:
        x -= dist
    elif direc == 2:
        y -= dist
    elif direc == 3:
        x += dist
    return (x, y)


def calc(moves):
    (x, y) = (0, 0)
    direc = 0
    for move in moves:
        if move == 'L':
            direc = (direc + 1) % 4
        elif move == 'R':
            direc = (direc - 1) % 4
        else:
            (x, y) = make_move(x, y, direc, move)
    return (x, y)


def string(dist):
    d = str(dist)
    k = d.find('.')
    return d[:k + 2]


cases = int(input())
for case in range(cases):
    movestr = input().replace(' ', '')
    moves = parse(movestr)
    (x, y) = calc(moves)
    dist = (x ** 2 + y ** 2) ** 0.5
    if x == 0:
        if y == 0:
            direc = ''
        elif y < 0:
            direc = 'S'
        else:
            direc = 'N'
    elif x < 0:
        if y == 0:
            direc = 'W'
        elif y < 0:
            direc = 'SW'
        else:
            direc = 'NW'
    elif y == 0:
        direc = 'E'
    elif y < 0:
        direc = 'SE'
    else:
        direc = 'NE'
    print('%s%s' % (string(dist), direc))
