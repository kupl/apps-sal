class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        s = set()
        for i in range(1, n + 1):
            for j in range(1, i):
                if i % j != 0 or j == 1:
                    if j / i not in s:
                        res.append(str(j) + '/' + str(i))
                        s.add(j / i)
        return res
