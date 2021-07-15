def cube_odd(arr):
    if any(type(x) is not int for x in arr):
        return None
    return sum(x ** 3 for x in arr if x % 2 != 0)
