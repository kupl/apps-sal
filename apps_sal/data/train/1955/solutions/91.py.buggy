from collections import defaultdict
class UF:
    
    def __init__(self,n):
        self.parent=[x for x in range(n)]
        
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        self.parent[self.find(x)]=self.find(y)


class Solution:       
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        \"\"\"
        0 1 2 3
        3 2
        2
        \"\"\"
        n=len(s)
        uf=UF(n)
        for item in pairs:
            uf.union(item[0],item[1])
        
        root_dict=defaultdict(list)
        
        for i,x in enumerate(list(s)):
            root_dict[uf.find(i)].append(x)
            
        for key in root_dict:
            root_dict[key]=sorted(root_dict[key],reverse=True)
            
        output=[]
        for i,x in enumerate(list(s)):
            output.append(root_dict[uf.find(i)].pop())
        
        return \"\".join(output)
        
