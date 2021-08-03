def cube_odd(n):
    return sum([el ** 3 for el in n if type(el) == int and el % 2 != 0]) if [el for el in n if type(el) != int] == [] else None
