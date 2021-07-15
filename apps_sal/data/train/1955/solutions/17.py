from collections import defaultdict

class Solution:
    def find(self,x):
        if(x!=self.parent[x]):
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
        
        
    def union(self,x,y):
        x_find=self.find(x)
        y_find=self.find(y)
        self.parent[x_find]=y_find
        
    
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n=len(s)
        self.parent=list(range(n))
        
        for x,y in pairs:
            self.union(x,y)
        
        # print(self.parent)
        
        groups=defaultdict(list)
        for i in range(n):
            tem=self.find(i)
            # self.parent[i]=tem
            groups[tem].append(s[i])    
            # print(tem)
        # print(self.parent)
        
        ans=[]
        for comp_id in groups.keys(): 
            groups[comp_id].sort(reverse=True)
            
        # print(groups)
        
        for i in range(n): 
            ans.append(groups[self.find(i)].pop())
        return \"\".join(ans)
        
