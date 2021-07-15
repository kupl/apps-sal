def even_or_odd(value):
    value2 = 2
    result = value % value2

    if result == 0:
        result_real = "Even"
    else:
        result_real = "Odd"
    return result_real
