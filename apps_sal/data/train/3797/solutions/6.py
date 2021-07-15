def find_the_ball(pos, swaps):
    for swap in swaps:
        if pos in swap:
            pos = swap[1 - swap.index(pos)]
    return pos
