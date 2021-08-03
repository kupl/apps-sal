def sum_cubes(n):
    i = 1
    m = 0
    while i <= n:
        cube = i**3
        m = m + cube
        i = i + 1
    return m
