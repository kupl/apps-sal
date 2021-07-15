def max_number(n):
    digits = []
    while n:
        n, d = divmod(n, 10)
        digits.append(d)

    return sum(d * 10 ** i for i, d in enumerate(sorted(digits)))

