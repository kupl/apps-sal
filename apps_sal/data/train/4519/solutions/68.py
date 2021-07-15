def max_number(n):
    return int(''.join([x for x in sorted(list(str(n)),reverse=True)]))
