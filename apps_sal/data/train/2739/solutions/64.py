def cube_odd(arr):
    if all(type(i) == int for i in arr): return sum((i**3) for i in arr if i%2 != 0)

