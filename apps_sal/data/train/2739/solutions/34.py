def cube_odd(arr):
    odd = list()
    for i in arr:
        if isinstance(i, int) and (not isinstance(i, bool)):
            if abs(i) % 2 != 0:
                odd.append(i)
        else:
            return None
    return sum(map(lambda x: x ** 3, odd))
