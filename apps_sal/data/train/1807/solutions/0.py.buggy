class Solution:
    arr = []
    
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        
        if len(Solution.arr) < 2:
            Solution.arr = [[],[]]
            
        if n >= len(Solution.arr):
            for d in range(len(Solution.arr), n + 1):
                denominator = \"/\" + str(d)
                Solution.arr.append([])
                
                for num in range(1, d):
                    if gcd(num, d) == 1:
                        Solution.arr[-1].append(str(num) + denominator)
                    
                    
        for i in range(2, n + 1):
            ans += Solution.arr[i]
                
        return ans
                    
                
        
