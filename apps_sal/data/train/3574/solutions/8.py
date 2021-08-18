def Dragon(n, Curve='Fa'):
    if type(n) != int or n % 1 != 0 or n < 0:
        return ''

    elif n == 0:
        return Curve.replace('a', '').replace('b', '')
    else:
        return Dragon(n - 1, Curve.replace('a', 'c').replace('b', 'd').replace('c', 'aRbFR').replace('d', 'LFaLb'))
