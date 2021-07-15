def array_madness(a,b):
    sum_squares = 0
    sum_cubes = 0
    for number in a:
        sum_squares += number  ** 2
    for number in b:
        sum_cubes += number ** 3
    if sum_squares > sum_cubes:
        return True
    return False
