class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        
        def gcd(a, b):
            if a==0:
                return b
            return gcd(b%a, a)
            
        for i in range(1, n):
            for j in range(i+1, n+1):
                if gcd(i,j)==1:
                    res.append(str(i)+\"/\"+str(j))
        
        return res
