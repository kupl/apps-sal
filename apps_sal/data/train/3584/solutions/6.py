def crypt(s, key, to_encrypt=True):
    keys = []
    for key in '{:0>3}'.format(key):
        keys.extend([int(key)] * 2)
    rows = ('qwertyuiop', 'QWERTYUIOP',
            'asdfghjkl', 'ASDFGHJKL',
            'zxcvbnm,.', 'ZXCVBNM<>')
    original = ''.join(rows)
    shifted = ''.join(r[k:] + r[:k] for r, k in zip(rows, keys))
    table = str.maketrans(*(
        (original, shifted) if to_encrypt else (shifted, original)))
    return s.translate(table)


def decrypt(s, key):
    return crypt(s, key, to_encrypt=False)


def encrypt(s, key):
    return crypt(s, key, to_encrypt=True)
