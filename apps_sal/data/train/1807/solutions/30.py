class Solution:

    def simplifiedFractions(self, n):
        res = []
        tmp = set()
        for i in range(1, n + 1):
            for x in range(1, i + 1):
                if x % i != 0 and x / i not in tmp:
                    tmp.add(x / i)
                    res.append(str(x) + '/' + str(i))
        return res
