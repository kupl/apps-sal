def cube_odd(arr):
    l = []
    for x in arr:
        if type(x) != int:
            return None
        elif x % 2 == 1:
            l.append(x ** 3)
    return sum(l)
