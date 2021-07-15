class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def lar_com(a,b):
            a,b=max(a,b),min(a,b)
            if b==0: return 0
            if b==1: return 1
            return lar_com(a-b,b)
            
        
        res=[]
        for i in range(2,n+1):
            for j in range(1,i):
                if lar_com(i,j)==1:
                    res.append(str(j)+\"/\"+str(i))
        return res
