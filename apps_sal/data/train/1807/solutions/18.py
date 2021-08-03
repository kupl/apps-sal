def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if gcd(i, j) == 1:
                    res.append('{}/{}'.format(i, j))
        return res
