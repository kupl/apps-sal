from itertools import compress


def grille(message, code):
    n = len(message)
    grille = map(int, '{:0{}b}'.format(code, n)[-n:])
    return ''.join(compress(message, grille))
