def decode(c, k):
    return ''.join((chr(a - int(b) + 96) for (a, b) in zip(c, str(k) * 30)))
