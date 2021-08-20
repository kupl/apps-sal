def array_madness(a, b):
    squares_list = [i ** 2 for i in a]
    cubes_list = [i ** 3 for i in b]
    return sum(squares_list) > sum(cubes_list)
