def convert(n):
    return ''.join([chr(int(i + k)) for (i, k) in zip(n[::2], n[1::2])])
