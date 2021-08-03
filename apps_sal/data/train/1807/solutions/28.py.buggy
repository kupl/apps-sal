class Solution:
    def is_coprime(self, a, b):
        l = max(a, b)
        s = min(a, b)
        
        while s > 0:
            l,s = s, l % s
        
        return l == 1
    
    def simplifiedFractions(self, n: int) -> List[str]:
      
        
        ans = []
        for d in range(2, n+1):
            n = 1
            while n < d:
                if n == 1 or self.is_coprime(n, d):
                    ans.append(str(n) + \"/\" + str(d))
                n += 1
        
        return ans
