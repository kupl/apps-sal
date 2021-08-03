from functools import partial


def code(mode, text, key):
    alphabet = "qwertyuiop asdfghjkl zxcvbnm,. QWERTYUIOP ASDFGHJKL ZXCVBNM<>"
    idxs = [mode * int(d) for d in '%03d' % key * 2]
    table = ' '.join(w[i:] + w[:i] for i, w in zip(idxs, alphabet.split()))
    return text.translate(str.maketrans(alphabet, table))


encrypt, decrypt = partial(code, 1), partial(code, -1)
