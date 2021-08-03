def array_madness(a, b):
    return sum(pow(el, 2) for el in a) > sum(pow(el, 3) for el in b)
