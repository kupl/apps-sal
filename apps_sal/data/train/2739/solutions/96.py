def cube_odd(arr):
    if all(isinstance(x, int) for x in arr) \
       and not any(isinstance(x, bool) for x in arr):
        return sum([x ** 3 for x in arr if x % 2])
    else:
        return None
