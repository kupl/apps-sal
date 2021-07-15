class Solution:
    def findLucky(self, arr: List[int]) -> int:
        t=[]
        x=collections.Counter(arr)
        for j,v in list(x.items()):
            if j==v:
                t.append(j)
        if len(t)!=0:
            return max(t)
        else:
            return -1
        
                
            
           
        
        
            
        
            
        

