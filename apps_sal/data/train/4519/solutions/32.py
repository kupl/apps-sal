def max_number(n):
    to_return = sorted(str(n), reverse=True)
    return int(''.join(to_return))
