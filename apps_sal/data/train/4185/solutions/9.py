def sc(w, l, g):
    return 0 if (2 * w + 2 * l - 4) % (g + 1) != 0 else (2 * w + 2 * l - 4) / (g + 1)
