class Solution:
    def solve(self, x):
        a = max(1, int(math.sqrt(x)))
        b = x // a
        while (a * b) != x:
            a = max(1, a - 1)
            b = x // a
        return [a, b]

    def closestDivisors(self, x):
        a, b = self.solve(x + 1)
        c, d = self.solve(x + 2)
        return [a, b] if (b - a) <= (d - c) else [c, d]
