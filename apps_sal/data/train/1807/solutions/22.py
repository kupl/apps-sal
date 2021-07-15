class Solution:
    def gcd(self, a, b):
        c = 1
        while c != 0:
            c = a % b
            a = b
            b = c
        return a
    def simplify(self, a, b):
        d = self.gcd(a, b)
        return (a // d, b // d)
    def simplifiedFractions(self, n):
        fractions = set()
        for denom in range(1, n + 1):
            for num in range(1, denom):
                expr = '%d/%d' % self.simplify(num, denom)
                if expr not in fractions:
                    fractions.add(expr)
        return list(fractions)

