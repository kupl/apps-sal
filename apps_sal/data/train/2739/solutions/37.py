def cube_odd(arr):
    for i in arr:
        if type(i) != type(1):
            return None
    return sum((i ** 3 for i in arr if i % 2 == 1))
