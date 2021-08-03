class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def hcfnaive(a,b): 
            if(b==0): 
                return a 
            else: 
                return hcfnaive(b,a%b) 
        ans = []
        for j in range(1,n+1):
            for i in range(1,j):
                igcd = hcfnaive(i,j)
                top,botm = i//igcd,j//igcd
                if top==1 and botm==1:
                    continue
                else:
                    temp = str(top)+\"/\"+str(botm)
                    if temp not in ans:
                        ans.append(temp)
        return ans
