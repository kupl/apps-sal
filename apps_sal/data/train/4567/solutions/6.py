def pillow(s):
    return next((True for a, b in zip(*s) if a == 'n' and b == 'B'), False)
