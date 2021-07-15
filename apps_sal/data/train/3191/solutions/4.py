def decode(code, key):
    k = [int(k) for k in str(key)]
    n = len(k)
    return ''.join(chr(c - k[i % n] + 96) for i, c in enumerate(code))
