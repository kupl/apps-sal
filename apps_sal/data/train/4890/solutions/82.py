def find_difference(a, b):
    cube1 = 1
    cube2 = 1
    for x in a:
        cube1 = cube1 * x
    for y in b:
        cube2 = cube2 * y
    if cube1 >= cube2:
        return cube1 - cube2
    else:
        return cube2 - cube1
