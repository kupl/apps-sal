def sum_digits(x):
    if len(str(x)) == 1:
        return x
    suma = 0
    for j in str(x):
        if j != '-':
            suma += int(j)
    return suma    # ...
