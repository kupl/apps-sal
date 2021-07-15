def array_madness(a,b):
    square = [ x ** 2 for x in a ]
    cube = [ y ** 3 for y in b ]
    return True if sum(square) > sum(cube) else False
