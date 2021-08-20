D_TUNE = {0, 2, 4, 5, 7, 9, 11}


def is_tune(notes):
    return bool(notes) and any(({(n - v) % 12 for v in notes} <= D_TUNE for n in range(12)))
