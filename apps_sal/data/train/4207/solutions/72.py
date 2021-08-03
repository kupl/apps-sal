def sum_cubes(n):
    counter = 0
    saver = 0
    while counter <= n:
        saver = counter**3 + saver
        counter += 1

    return saver
