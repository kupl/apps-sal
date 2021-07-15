def max_number(n):
    return int("".join(map(str,sorted((int(n) for n in str(n)), reverse=True))))
