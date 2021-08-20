def max_number(n):
    x = ','.join(str(n)).split(',')
    x1 = sorted(x)
    return int(''.join(x1)[::-1])
