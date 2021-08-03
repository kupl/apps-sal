def sum_cubes(n):
    result = 0
    for cube in range(n + 1):
        result = result + cube * cube * cube
    return result
