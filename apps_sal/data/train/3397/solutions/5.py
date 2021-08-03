from itertools import compress


def grille(message, code):
    l = len(message)
    code = list(map(int, bin(code)[2:].zfill(l)))
    return ''.join(list(compress(message, [code, code[l:]][l < len(code)])))
