def array_madness(a, b):
    return sum((i ** 2 for i in a)) > sum((i ** 3 for i in b))
