def get_participants(h):
    n = 0
    counter = 0
    while h > 0:
        h -= counter
        n += 1
        counter += 1
    return n or 1
