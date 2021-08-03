keyboard = [
    'abcde123',
    'fghij456',
    'klmno789',
    'pqrst.@0',
    'uvwxyz_/',
]
positions = {ch: (r, c) for r, row in enumerate(keyboard) for c, ch in enumerate(row)}


def tv_remote(word):
    r, c = 0, 0
    presses = 0
    for ch in word:
        r2, c2 = positions[ch]
        presses += abs(r2 - r) + abs(c2 - c) + 1
        r, c = r2, c2
    return presses
