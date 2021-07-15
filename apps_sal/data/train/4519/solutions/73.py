def max_number(n):
    x = sorted(list(str(n)),reverse=True)
    return int(''.join(i for i in x))
