def sum_of_minimums(n):
    c = 0
    for i in n:
        c += min(i)
    return c
