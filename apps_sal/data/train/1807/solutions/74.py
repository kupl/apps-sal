class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        num_res = []
        for i in range(1,n+1):
            for j in range(1,i):
                if i/j not in num_res:
                    res.append(str(j)+'/'+str(i))
                    num_res.append(i/j)
        return res
