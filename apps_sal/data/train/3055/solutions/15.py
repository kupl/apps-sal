def sum_str(a, b):
    a = a if a != '' else 0
    b = b if b != '' else 0
    return str(sum(map(int, [a, b])))
