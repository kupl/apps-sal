def find(n):
    s = 0

    for x in range(0, n + 1):
        if x % 3 == 0 or x % 5 == 0:
            s += x
    return(s)
