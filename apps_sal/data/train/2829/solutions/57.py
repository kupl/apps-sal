def array_madness(a, b):
    return True if sum((n ** 2 for n in a)) > sum((n ** 3 for n in b)) else False
