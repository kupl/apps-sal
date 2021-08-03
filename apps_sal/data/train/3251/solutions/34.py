def primeFactors(n):
    factors = []
    p = 2
    while n != 1 and p <= n**0.5:
        if n % p == 0:
            factors.append(p)
            n = n // p
        else:
            p = p + 1
    if n != 1:
        factors.append(n)
        n = 1

    distinct = sorted(set(factors))

    answer = ""
    for prime in distinct:
        if factors.count(prime) == 1:
            answer = answer + "(" + str(prime) + ")"
        else:
            answer = answer + "(" + str(prime) + "**" + str(factors.count(prime)) + ")"

    return answer
