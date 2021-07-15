def find_the_ball(pos, swaps):
    for a, b in swaps:
        pos = a if pos == b else b if pos == a else pos
    return pos
