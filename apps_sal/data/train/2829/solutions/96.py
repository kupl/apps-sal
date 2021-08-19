def array_madness(a, b):
    return sum((i * i for i in a)) > sum((w * w * w for w in b))
