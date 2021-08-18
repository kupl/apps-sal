def find_difference(a, b):
    cube1 = a[0] * a[1] * a[2]
    cube2 = b[0] * b[1] * b[2]
    result = cube1 - cube2
    if cube1 - cube2 < 0:
        result = cube2 - cube1
    return result
