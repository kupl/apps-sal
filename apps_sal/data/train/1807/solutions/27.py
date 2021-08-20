class Solution:

    def euclid(self, a, b):
        if b == 0:
            return a
        else:
            return self.euclid(b, a % b)

    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for d in range(2, n + 1):
            for n in range(1, d):
                if self.euclid(n, d) > 1:
                    continue
                res.append(str(n) + '/' + str(d))
        return res
