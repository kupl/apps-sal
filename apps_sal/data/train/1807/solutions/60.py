class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def maxm(n1, n2):
            temp = min(n1, n2)
            while temp:
                if n1 % temp == 0 and n2 % temp == 0:
                    return temp
                temp -= 1

        res = []
        for j in range(2, n + 1):
            for i in range(1, j):
                if maxm(j, i) > 1:
                    continue
                res.append(str(i) + '/' + str(j))
        return res
