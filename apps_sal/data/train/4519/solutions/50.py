def max_number(n):
    y = []
    for x in str(n):
        y.append(x)

    return int(''.join(sorted(y, reverse=True)))
