def cube_odd(arr):
    return sum(n**3 for n in arr if n % 2 == 1) if all(type(e) == int for e in arr) else None
