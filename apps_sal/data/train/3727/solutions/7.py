def factors(n, limit):
    return [i for i in range(2, limit + 1) if n % i == 0]


def pythagorean_triplet(n):
    for x in factors(n, int(n**(1 / 3))):
        nn = n // x
        for y in factors(nn, int(nn**(1 / 2))):
            z = nn // y
            if x * x + y * y == z * z:
                return [x, y, z]
