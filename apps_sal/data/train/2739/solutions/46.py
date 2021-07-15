def cube_odd(arr):
    cubes = []
    for i in arr:
        if type(i)!=int:
            return None
        if i%2!=0:
            cubes.append(i**3)
    return sum(cubes)
