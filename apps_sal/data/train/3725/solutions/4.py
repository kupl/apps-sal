import os

def shift_left(a, b):
    x = os.path.commonprefix([a[::-1], b[::-1]])
    return len(a) + len(b) - len(x) * 2
