def cube_odd(arr):
    result = 0
    for n in arr:
        if type(n) == type('s') or type(n) == type(True):
            return None
        elif n ** 3 % 2 != 0 and type(n) == type(5):
            result += n ** 3
    return result
