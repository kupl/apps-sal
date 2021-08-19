def max_number(n):
    integers = sorted([int(i) for i in str(n)])
    return sum((v * 10 ** i for (i, v) in enumerate(integers)))
