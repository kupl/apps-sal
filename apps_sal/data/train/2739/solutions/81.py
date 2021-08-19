def cube_odd(arr):
    return sum((x ** 3 for x in arr if x % 2)) if all((isinstance(x, int) and (not isinstance(x, bool)) for x in arr)) else None
