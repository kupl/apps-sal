def cube_odd(arr):
    return sum((x ** 3 for x in arr if x % 2)) if all((type(x) is int for x in arr)) else None
