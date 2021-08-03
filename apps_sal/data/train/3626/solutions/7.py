def encode(s, key):
    D = {key[i]: key[i + 1] for i in range(0, len(key), 2)}
    D.update({v: k for k, v in D.items()})
    D.update({k.upper(): v.upper() for k, v in D.items()})
    return s.translate(str.maketrans(D))


decode = encode
