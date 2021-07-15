def reorder(a, b):
    a >>= 1
    b %= a
    return [[d+(i-b)%a for i in range(a)] for d in (0,a)]
