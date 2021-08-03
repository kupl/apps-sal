class Solution:
    def solve(self, x):
        a = max(1, int(math.sqrt(x)))
        while (a * (x // a)) != x:
            a = max(1, a - 1)
        return [a, x // a]

    def closestDivisors(self, x):
        a, b = self.solve(x + 1)
        if a == b:
            return [a, b]
        c, d = self.solve(x + 2)
        return [a, b] if (b - a) <= (d - c) else [c, d]
