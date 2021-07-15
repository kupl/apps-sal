def cube_odd(arr):
    if set(map(type, arr)) != {int}:
        return None
    return sum([y for y in [x**3 for x in arr] if y % 2 == 1])
