def pythagorean_triplet(n):
    from math import sqrt

    def divisors(n):
        divs = []
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                divs.append(i)
        divs.sort()
        return divs
    divs = divisors(n)
    for a in divs:
        for b in divs:
            c = n // (a * b)
            if a * a + b * b == c * c:
                return [a, b, c]
