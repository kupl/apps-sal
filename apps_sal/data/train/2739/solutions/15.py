def cube_odd(arr):
    a = sum([el**3 for el in arr if type(el) == int and el % 2 != 0])
    return a if [el for el in arr if type(el) != int] == [] else None
