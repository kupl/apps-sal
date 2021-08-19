def f(n):
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            n = n / i
            factors.append(i)
        else:
            i += 1
    from collections import Counter
    from numpy import prod
    return prod([occurences * factor ** (occurences - 1) for (factor, occurences) in Counter(factors).items()])
