class Solution:

    def simplifiedFractions(self, n: int) -> List[str]:

        def gcd(i, j):
            (i, j) = sorted([i, j])
            if j % i == 0:
                return i
            return gcd(i, j % i)
        res = []
        for d in range(1, n + 1):
            for n in range(1, n + 1):
                if 0 < n / d < 1 and gcd(d, n) == 1:
                    res.append('{}/{}'.format(n, d))
        return res
