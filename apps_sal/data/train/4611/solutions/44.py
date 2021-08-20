def animals(h, l):
    cow = (l - 2 * h) / 2
    ch = h - cow
    return 'No solutions' if cow < 0 or ch < 0 or (not cow.is_integer()) or (not ch.is_integer()) else (ch, cow)
