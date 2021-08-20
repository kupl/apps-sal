class Solution:

    def simplifiedFractions(self, n: int) -> List[str]:
        from fractions import Fraction
        p = []
        if n == 1:
            return
        for numerator in range(1, n):
            k = str(1) + '/' + str(numerator + 1)
            p.append(k)
        for numerator in range(2, n + 1):
            for denominator in range(numerator + 1, n + 1):
                b = Fraction(numerator, denominator)
                b = str(b)
                if b not in p:
                    k = str(numerator) + '/' + str(denominator)
                    p.append(k)
        return p


def isprime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True
