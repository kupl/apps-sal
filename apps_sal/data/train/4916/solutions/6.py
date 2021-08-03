import gmpy2


def get_primes(how_many, group_size):
    n = 2
    count = 0
    while count < how_many:
        res = []
        for i in range(group_size):
            res.append(int(n) if count < how_many else None)
            n = gmpy2.next_prime(n)
            count += 1
        yield tuple(res)
