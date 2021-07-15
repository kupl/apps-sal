class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = [i for i in range(n)]
        
        for u, v in pairs:
            self.union(parent, u, v)
        
        m = collections.defaultdict(list)
        for i in range(n):
            m[self.find_root(parent, i)].append(i)
        
        ans = list(s)
        for _, indices in m.items():
            temp = []
            for i in indices:
                temp.append(s[i])
            temp.sort()
            for i in range(len(temp)):
                ans[indices[i]] = temp[i]
        
        return \"\".join(ans)
    
    def find_root(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find_root(parent, parent[x])
        return parent[x]
    
    def union(self, parent, x, y):
        x_root = self.find_root(parent, x)
        y_root = self.find_root(parent, y)
        if x_root != y_root:
            parent[x_root] = y_root
