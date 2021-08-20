def two_decimal_places(n):
    num = round(n, 4)
    n1 = str(num)
    if n1[-1] == '5':
        n1 = n1[:-1] + '6'
        return round(float(n1), 2)
    else:
        return round(n, 2)
