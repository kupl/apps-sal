def cube_odd(arr):
    for x in arr:
        if type(x) != int: return None
    return sum([x**3 for x in arr if x**3 % 2 != 0])
