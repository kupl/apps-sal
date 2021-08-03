def array_madness(a, b):
    square = [x**2 for x in a]
    cube = [x**3 for x in b]
    return sum(square) > sum(cube)
