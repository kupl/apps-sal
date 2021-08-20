def cube_odd(arr):
    if any((isinstance(v, bool) or not isinstance(v, int) for v in arr)):
        return
    return sum((v ** 3 for v in arr if v % 2))
