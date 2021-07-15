def find_difference(a, b):
    cube_a = cube_b = 1
    for x in a: cube_a *= x
    for x in b: cube_b *= x
    return abs(cube_a - cube_b)
