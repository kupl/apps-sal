class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        if n == 1:
            return []
        
        rst = []
        
        dedup = set()
        
        for i in range(1, n+1):
            
            for j in range(1, i):
                
                x = j/i
                
                s = str(j) + \"/\" + str(i)
                
                print(s)
                
            
                if x not in dedup:

                    dedup.add(x)
                    rst.append(s)
                    
        return rst
        
