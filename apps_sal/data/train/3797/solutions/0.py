def find_the_ball(start, swaps):
    pos = start
    for (a, b) in swaps:
        if a == pos:
            pos = b
        elif b == pos:
            pos = a
    return pos
