import math
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        if n == 1: return res
        for i in range(2,n+1):
            for j in range(1,i):
                if math.gcd(i,j) == 1: 
                    res.append(f\"{j}/{i}\")
        return res
                               
                
            
        
