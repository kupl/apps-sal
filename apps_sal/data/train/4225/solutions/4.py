def cup_and_balls(b, arr):
    for swap in arr:
        if b in swap:
            b = swap[not swap.index(b)]
    return b
