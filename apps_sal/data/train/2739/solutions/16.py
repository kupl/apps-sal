def cube_odd(arr):
    for el in arr:
        if type(el) != int:
            return None
    return sum([el ** 3 for el in arr if type(el) == int and el % 2 != 0])
