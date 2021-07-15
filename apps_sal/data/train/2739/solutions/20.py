def cube_odd(arr):
    cube = []
    for i in arr:
        if type(i) != int:
            return None
        if i % 2 != 0:
            cube.append(i**3)
    return sum(cube)

