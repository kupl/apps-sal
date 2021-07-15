def cube_odd(arr):
    if all(map(lambda x: type(x) is int, arr)):
        return sum(map(lambda x: x ** 3, filter(lambda x: x % 2, arr)))
    return None
