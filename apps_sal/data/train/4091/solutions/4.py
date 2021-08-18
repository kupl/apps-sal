ks = ['A', 'A
keys = ks * 7 + ks[:4]


def which_note(n):
    return keys[(n - 1) % len(keys)]
