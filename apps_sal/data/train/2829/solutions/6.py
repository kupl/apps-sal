def array_madness(a, b):
    return sum(map(lambda x: x ** 2, a)) > sum(map(lambda x: x ** 3, b))
