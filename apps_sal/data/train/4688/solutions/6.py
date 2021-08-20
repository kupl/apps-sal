def expanded_form(n):
    (integer, decimal) = str(n).split('.')
    l = len(integer)
    integer = [f"{digit}{'0' * (l - i)}" for (i, digit) in enumerate(integer, 1) if digit != '0']
    decimal = [f"{digit}/1{'0' * i}" for (i, digit) in enumerate(decimal, 1) if digit != '0']
    return ' + '.join(integer + decimal)
