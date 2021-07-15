from collections import defaultdict
import math


class Solution:
    
                    
                    
    def simplifiedFractions(self, n: int) -> List[str]:
        
        
        if n == 1:
            return []
                    
        numer = defaultdict(list)     
        for i in range(2, 101):
            for j in range(1, i):
                if math.gcd(i, j) == 1:
                    numer[i].append(j)
        ans = []
        
        for i in range(2, n+1):
            for j in numer[i]:
                ans.append(f'{j}/{i}')
                
        print(ans)
        return ans

