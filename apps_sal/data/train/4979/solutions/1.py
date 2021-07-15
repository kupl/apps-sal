from math import copysign

directions = {
    '←': (0, -1),
    '↑': (-1, 0),
    '→': (0, 1),
    '↓': (1, 0),
    '↖': (-1, -1),
    '↗': (-1, 1),
    '↘': (1, 1),
    '↙': (1, -1),
}

def count_deaf_rats(town_square):
    pi, pj = next((i,j) for i, row in enumerate(town_square) for j, x in enumerate(row) if x == 'P')
    result = 0
    for i, row in enumerate(town_square):
        for j, x in enumerate(row):
            if x not in directions:
                continue
            di, dj = directions[x]
            if (i+di-pi)**2 + (j+dj-pj)**2 > (i-pi)**2 + (j-pj)**2:
                result += 1
    return result
