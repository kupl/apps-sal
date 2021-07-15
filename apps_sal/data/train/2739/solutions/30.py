def cube_odd(arr):
    a = [i for i in arr if type(i) == int]
    return sum([i**3 for i in a if i % 2 == 1]) if len(a) == len(arr) else None
