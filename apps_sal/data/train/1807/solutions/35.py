class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        fin=[]
        for i in range(2,n+1):
            for j in range(1,i):
                if(gcd(i,j)==1):
                    fin.append(str(j)+'/'+str(i))
        return fin
