def cube_odd(arr):
    cubes = []
    for item in arr:
        if str(item).strip('-').isdigit() == False:
            return None
        elif item % 2 != 0:
            cubes.append(item ** 3)
    return sum(cubes)
