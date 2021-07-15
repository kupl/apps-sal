def multiply(a,b):
    a_start = a
    for s in range(0, b-1):
        a += a_start
    return a

