def cube_odd(arr):
    return None if any([type(i) != int for i in arr]) else sum((i**3 for i in arr if i % 2 == 1))
