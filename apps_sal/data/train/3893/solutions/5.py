def divisors(n):
    divs = set()
    for t in range(2, int(n ** 0.5) + 1):
        (div, mod) = divmod(n, t)
        if mod == 0:
            divs.add(t)
            divs.add(div)
    return '{:d} is prime'.format(n) if len(divs) == 0 else sorted(list(divs))
