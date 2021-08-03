def faro_cycles(size):
    deck = list(range(size))
    cur, count = deck[::2] + deck[1::2], 1
    while cur != deck:
        cur, count = cur[::2] + cur[1::2], count + 1
    return count
