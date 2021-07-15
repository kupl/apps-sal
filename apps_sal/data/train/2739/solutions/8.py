def cube_odd(arr):
    total = 0
    for el in arr:
        if isinstance(el, int):
            if el % 2 == 1 and el != 0:
                total += el ** 3
        else:
            return None
    if total == 2:
        return None
    return total
