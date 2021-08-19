def four_piles(n, y):
    x = n * y / (2 * y + y * y + 1)
    lst = [x + y, x - y, x * y, x / y]
    return lst if all((v > 0 and v.is_integer() for v in lst)) else []
