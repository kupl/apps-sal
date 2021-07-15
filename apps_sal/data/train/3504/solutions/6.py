def power_mod(x, y, n):
    x = x%n
    b = bin(y)[2:]
    l = len(b)
    res = [0]*l
    for i in range(l):
        res[-i-1] = x
        x *= x
        x = x%n
    prod = 1
    for i in range(l):
        if b[-i-1] == '1':
            prod *= res[-i-1]
            prod = prod%n
    return prod
