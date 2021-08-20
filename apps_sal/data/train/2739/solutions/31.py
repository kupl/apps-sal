def cube_odd(arr):
    for i in arr:
        if type(i) != int:
            return None
    return sum([i ** 3 for i in arr if i % 2])
