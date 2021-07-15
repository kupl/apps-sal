class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        d={i:i-1 for i in range(1,m+1)}
        ans=[]
        for i in queries:
            x=d[i]
            ans.append(x)
            
            for j in list(d.keys()):
                if d[j]<x:
                    d[j]+=1
            d[i]=0
        
        return ans
            
                    
             
            
        

