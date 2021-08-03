def cube_odd(arr):
    if len([el for el in arr if type(el) != int]) > 0:
        return None
    return sum([el ** 3 for el in arr if el % 2 != 0])
