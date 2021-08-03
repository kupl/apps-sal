def cube_odd(arr):
    x = []
    for i in arr:
        if type(i) != int:
            return None
        elif type(i) == int and i % 2 != 0:
            x.append(i**3)

    return sum(x)
