class DUS:
    def __init__(self, N):
        self.N = N
        self.p = [i for i in range(self.N)]
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x] 

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.p[rooty] = rootx

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        ans = \"\"   
        dict_components = collections.defaultdict(list)
        N = len(s)
        dus = DUS(N)
        
        for x, y in pairs: 
            dus.union(x, y)

        for i in range(len(s)):
            dict_components[dus.find(i)].append(s[i])
            
        for comp_id in dict_components.keys():
            dict_components[comp_id].sort()

            
        for i in range(len(s)):
            char = dict_components[dus.find(i)].pop(0)
            ans = ans + char
        
        return ans
            
      
            
            
            
            
            
            
            
            
            
            
            
            
            
        
