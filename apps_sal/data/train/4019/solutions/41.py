def max_multiple(divisor, bound):
    new = []
    for n in range(1000000):
        if n % divisor == 0 and n <= bound:
            new.append(n)
    return max(new)
