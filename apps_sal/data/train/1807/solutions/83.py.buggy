class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n==1: return []
        a=[]
        ans=[]
        for i in range(1,n):
            for j in range(i+1,n+1):
                if i/j not in a:
                    a.append(i/j)
                    ans.append(str(i)+\"/\"+str(j))
                    
        return ans
                
