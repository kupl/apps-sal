def cube_odd(arr):
    sum = 0
    for x in arr:
        if (not isinstance(x, (int, float, complex)) or isinstance(x, bool)): return None
        if (x % 2 == 1): sum += x ** 3
    return sum
