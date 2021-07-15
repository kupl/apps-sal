def factors(n):
    divisors = [i for i in range(2, n+1)if n % i == 0]
    sq = [x for x in divisors if x**2 in divisors]
    qb = [x for x in divisors if x**3 in divisors]
    return [sq, qb] or [[], []]
