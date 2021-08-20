def decode(code, key):
    k = str(key)
    while len(k) < len(code):
        k *= 2
    return ''.join((chr(x - int(y) + 96) for (x, y) in zip(code, k)))
