def getTriplets(n):
    divs = {y for x in range(1, int(n**.5) + 1) for y in (x, n // x) if not n % x}
    for a in divs:
        for b in divs:
            if n / a / b in divs:
                yield sorted((a, b, n / (a * b)))


def pythagorean_triplet(n):
    return next([a, b, c] for a, b, c in getTriplets(n) if a**2 + b**2 == c**2)
