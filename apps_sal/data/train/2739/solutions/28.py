def cube_odd(arr):
    while all(type(d) == int for d in arr):
        return sum(d**3 for d in arr if (d**3) % 2 == 1)
