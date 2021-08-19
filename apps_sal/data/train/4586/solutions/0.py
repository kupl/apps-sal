KEYBOARD = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
MAP = {c: (i // 8, i % 8) for (i, c) in enumerate(KEYBOARD)}


def manhattan(*pts):
    return sum((abs(z2 - z1) for (z1, z2) in zip(*pts)))


def tv_remote(word):
    return len(word) + sum((manhattan(MAP[was], MAP[curr]) for (was, curr) in zip('a' + word, word)))
