def gcd(a,b):
    if a == 0:
        return b
    
    if b == 0:
        return a
    
    if a == b:
        return a
    
    if a > b:
        return gcd(a-b,b)
    return gcd(a,b-a)

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n == 1:
            return []
        res = []
        
        for i in range(2,n+1):
            for j in range(1,i+1):
                if gcd(i,j) == 1:
                    s = str(j) + \"/\" + str(i)
                    res.append(s)
        return res
