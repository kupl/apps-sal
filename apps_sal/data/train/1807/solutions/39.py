class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a, b):
            if b == 0: return a
            return gcd(b, a%b)
        
        result = []
        for i in range(2, n+1):
            for j in range(i-1, 0, -1):
                if gcd(j, i) == 1:
                    result.append(\"{0}/{1}\".format(j,i))
        return result
                
        
