def max_number(n):
    # print(type(n))
    return int(''.join(sorted(str(n), reverse=True)))
