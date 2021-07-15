def sum_cubes(n):
    s = 1
    f = n
    v = 0
    while s != f + 1:
       v += s **3
       s += 1
    return v
