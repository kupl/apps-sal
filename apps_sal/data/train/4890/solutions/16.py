def find_difference(a, b):
    t1 = 1
    t2 = 1
    for num in a:
        t1 *= num
    for num in b:
        t2 *= num
    return abs(t1 - t2)
