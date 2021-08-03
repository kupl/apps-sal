def formatSquare(sq, isEncode):
    BASE = "ADFGX"
    dct = {c: BASE[i // 5] + BASE[i % 5] for i, c in enumerate(sq)}
    return dct if isEncode else {v: k for k, v in dct.items()}


def adfgx_utility(txt, sq, isEncode):
    dct, step = formatSquare(sq, isEncode), 2 - isEncode
    return ''.join(dct[txt[i:i + step]] if txt[i:i + step] in dct else dct['i'] for i in range(0, len(txt), step))


def adfgx_encrypt(plaintext, square): return adfgx_utility(plaintext, square, True)
def adfgx_decrypt(ciphertext, square): return adfgx_utility(ciphertext, square, False)
