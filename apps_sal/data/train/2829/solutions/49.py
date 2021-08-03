def array_madness(a, b):
    squares = sum([el ** 2 for el in a])
    cubes = sum([el ** 3 for el in b])
    return squares > cubes
