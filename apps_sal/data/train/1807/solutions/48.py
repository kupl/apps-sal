class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for i in range(2, n+1):
            for j in range(1, i):
                found = False
                for k in range(2, j+1):
                    if i % k == 0 and j % k == 0:
                        found = True
                        break
                if not found: ans.append(str(j) + \"/\" + str(i))
        return ans

