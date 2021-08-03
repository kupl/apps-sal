def faro_cycles(deck_size):
    if deck_size == 2:
        return 1
    pos, output = 2, 1
    while pos != 1:
        pos = pos * 2 % (deck_size - 1)
        output += 1
    return output
