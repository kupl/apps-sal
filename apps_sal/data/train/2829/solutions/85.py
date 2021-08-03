def square(x):
    return x * x


def Cube(x):
    return x * x * x


def array_madness(a, b):
    return ((True, False)[sum(map(square, a)) < sum(map(Cube, b))])
