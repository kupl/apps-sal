def powers_of_two(n):
    p = 1
    l = [ 1 ]
    for x in range(1, n+1):
        p *= 2;
        l.append(p)
    return l

