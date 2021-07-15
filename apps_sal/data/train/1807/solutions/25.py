class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        seen = set()
        res = []
        for j in range(2,n+1):
            for i in range(1,j):
                if i/j not in seen:
                    seen.add(i/j)
                    res.append(str(i)+\"/\"+str(j))
        return res
