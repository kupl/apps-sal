class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.parent = {i: i for i in range(len(s))}
        
        for pos1, pos2 in pairs:
            self.merge(pos1, pos2)
        
        connected_component = defaultdict(list)
        for i in range(len(s)):
            connected_component[self.find(i)].append(s[i])
        for k in connected_component.keys():
            connected_component[k].sort(reverse=True)
            
        res = []
        for i in range(len(s)):
            res.append(connected_component[self.find(i)].pop())
        
        return ''.join(res)
    
    
    def find(self, e):
        while e != self.parent[e]:
            self.parent[e] = self.parent[self.parent[e]]
            e = self.parent[e]
        return e
    
    def merge(self, e1, e2):
        root1, root2 = self.find(e1), self.find(e2)
        if root1 != root2:
            self.parent[root1] = root2
        
        return 
