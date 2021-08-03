def faro_cycles(deck_size):
    pos = 1
    for i in range(deck_size):
        pos = pos * 2 - (0 if pos < deck_size / 2 else deck_size - 1)
        if pos == 1:
            return i + 1
