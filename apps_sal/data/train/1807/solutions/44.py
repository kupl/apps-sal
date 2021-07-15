class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        seen = set()
        ans = []
        
        for i in range(2,n+1):
            for j in range(1,i):
                if j / i not in seen:
                    seen.add(j/i)
                    ans.append(\"%d/%d\" % (j,i))
                    
        return ans
        
