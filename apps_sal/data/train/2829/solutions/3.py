def array_madness(a, b):
    return True if sum([x**2 for x in a]) > sum([y**3 for y in b]) else False
