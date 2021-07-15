def reverse_number(n):
    x = str(n)
    if '-' in x:
        y = list(x)
        y.reverse()
        y.remove('-')
        return int(''.join(y)) * -1
    else:
        y = list(x)
        y.reverse()
        return int(''.join(y))
