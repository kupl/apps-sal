class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        simp = set()
        out = []
        for i in range(1,n+1):
            for j in range(1,i):
                if not j/i in simp:
                    out.append(f\"{j}/{i}\")
                    simp.add(j/i)
                    
        return out
        
