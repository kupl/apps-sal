class Solution:

    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for i in range(2, n + 1):
            res.append('1/' + str(i))
        for i in range(2, n):
            for j in range(i + 1, n + 1):
                if self.gcd(i, j) == 1:
                    res.append(str(i) + '/' + str(j))
        return res

    def gcd(self, a, b):
        while b:
            (a, b) = (b, a % b)
        return abs(a)
