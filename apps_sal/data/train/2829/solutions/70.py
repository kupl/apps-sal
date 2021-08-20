def array_madness(a, b):
    c = False
    sum1 = list(map(lambda number: number * number, a))
    sum2 = list(map(lambda number: number * number * number, b))
    if sum(sum1) > sum(sum2):
        c = True
    return c
