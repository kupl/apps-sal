def sc(w, l, g):
    return [0, (2 * (w + l) - 4) // (g + 1)][((2 * (w + l) - 4) % (g + 1)) == 0]
