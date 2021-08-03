def folding(a, b, c=0):
    return folding(b, a % b, c + a // b) if b != 0 else c
