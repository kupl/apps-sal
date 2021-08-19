def cube_odd(arr):
    return sum((n ** 3 for n in arr if n % 2 == 1)) if all((type(x) == int for x in arr)) else None
