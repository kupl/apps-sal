lower = 'abcdefghijklmnopqrstuvwxyz'


def one_down(txt):
    if not isinstance(txt, str):
        return 'Input is not a string'
    shifted = lower[-1] + lower[:-1]
    table = str.maketrans(lower + lower.upper(), shifted + shifted.upper())
    return txt.translate(table)
