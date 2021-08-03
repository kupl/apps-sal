def solomons_quest(arr):
    pos, lvl = [0, 0], 0
    for dilat, dir, dist in arr:
        lvl += dilat
        pos[dir in [0, 2]] += dist * 2**lvl * (-1)**(dir in [2, 3])
    return pos
