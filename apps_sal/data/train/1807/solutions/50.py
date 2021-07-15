class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        a=[]
        for i in range(2,n+1):
            s=\"1\"+\"/\"+str(i)
            a.append(s)
        for i in range(2,n):
            for j in range(2,n+1):
                if(math.gcd(i,j)==1 and (i/j)<1):
                    s=str(i)+\"/\"+str(j)
                    a.append(s)
        return a
        
