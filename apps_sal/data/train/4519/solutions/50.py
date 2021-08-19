def max_number(n):
    # your code here
    y = []
    for x in str(n):
        y.append(x)

    return int(''.join(sorted(y, reverse=True)))
