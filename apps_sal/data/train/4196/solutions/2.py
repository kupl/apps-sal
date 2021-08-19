def summationOfPrimes(primes: int):
    q = [2]
    for i in range(3, primes + 1, 2):
        for j in range(3, int(i ** 0.5) + 1, 2):
            if i % j == 0:
                break
        else:
            q.append(i)
    return sum(q)
