def cube_odd(arr):
    all_int = all((type(n) == int for n in arr))
    return sum((n ** 3 for n in arr if n & 1)) if all_int else None
