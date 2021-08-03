D = {a: b for a, b in zip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
                          'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM5678901234')}


def ROT135(s):
    return ''.join(D.get(c, c) for c in s)
