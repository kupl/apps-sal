def folding(a, b):
    return 0 if b == 0 else a // b + folding(b, a % b)
