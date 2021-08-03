def cube_odd(arr):
    return sum(n**3 for n in arr if n % 2) if all(type(n) == int for n in arr) else None
