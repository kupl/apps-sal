class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            for j in range(1,i):
                if gcd(i,j) == 1:
                    ans.append(str(j)+'/'+str(i))
        return ans
    
    def gcd(a,b):
        while a:
            a,b = b%a, a
        return b
