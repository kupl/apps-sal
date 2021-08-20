def sum_square_even_root_odd(l):
    return round(sum((x ** [2, 0.5][x & 1] for x in l)), 2)
