def is_tune(notes):
    SCALE = [1, 3, 5, 6, 8, 10, 0]
    for n in range(12):
        if all((note - n) % 12 in SCALE for note in notes):
            return bool(notes)
    return False
