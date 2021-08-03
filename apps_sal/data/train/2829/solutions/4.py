def array_madness(a, b):
    return sum(map(lambda x: x * x, a)) > sum(map(lambda x: x * x * x, b))
