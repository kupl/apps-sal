def list_squared(m, n):
    pool, sums = range(m, n), []

    for number in pool:
        divisors = [x for x in range(1, int(number**0.5 + 1)) if not number % x]
        divisors += [number / x for x in divisors if x != number / x]
        sums.append([number, sum([x**2 for x in divisors])])

    return [x for x in sums if x[1]**0.5 == int(x[1]**0.5)]
