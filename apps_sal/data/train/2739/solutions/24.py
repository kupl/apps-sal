def cube_odd(arr):
    s = [el for el in arr if type(el) != int]
    return sum([el ** 3 for el in arr if type(el) == int and el % 2 != 0]) if len(s) == 0 else None
