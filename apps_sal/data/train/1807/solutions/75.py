import itertools

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        num_res = []
        for i,j in itertools.permutations(range(1,n+1),2):
            if i/j < 1 and i/j not in num_res:
                res.append(str(i)+'/'+str(j))
                num_res.append(i/j)
                    
        return res
