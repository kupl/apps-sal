def gcd(a,b):     # Everything divides 0  
    if (a == 0): 
        return b 
    if (b == 0): 
        return a     # base case 
    if (a == b): 
        return a     # a is greater 
    if (a > b): 
        return gcd(a-b, b) 
    return gcd(a, b-a) 

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        finals = []
        for i in range(1, n):
            for j in range(i,n + 1):
                if i != j:
                    g = gcd(i, j)
                    finals.append(\"{}/{}\".format(i//g, j//g))        
        return list(set(finals))
        
