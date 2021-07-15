def max_number(num):
    n = list(str(num))
    sort_n = sorted(n)
    return int(''.join(sort_n[::-1]))
