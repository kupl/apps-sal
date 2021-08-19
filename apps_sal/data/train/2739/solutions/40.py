def cube_odd(arr):
    c = []
    n = []
    for x in arr:
        if type(x) != int:
            return None
        elif x < 0 and x % 2 != 0:
            c.append(x ** 3)
        elif x > 0 and x % 2:
            n.append(x ** 3)
    return sum(n) + sum(c)
