def array_madness(a, b):
    a_squares = [i ** 2 for i in a]
    b_cubes = [i ** 3 for i in b]
    return sum(a_squares) > sum(b_cubes)
