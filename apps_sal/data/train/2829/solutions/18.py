def array_madness(a, b):

    def s(x, y):
        return sum(list(map(lambda z: z ** y, x)))
    return s(a, 2) > s(b, 3)
