
        
class UF(object):
    
    def __init__(self):
        self.parent = [i for i in range(100001)]
        self.rank = [0]*100001
        
    def find(self, x):
        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        setx, sety = self.find(x), self.find(y)
        if setx == sety: return False
        elif self.rank[setx] < self.rank[sety]:
            self.parent[setx] = sety
        elif self.rank[sety] < self.rank[setx]:
            self.parent[sety] = setx
        else: 
            self.parent[sety] = setx
            self.rank[setx] += 1
        return True 

class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        \"\"\"
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        \"\"\"
        u, graph, groups, res = UF(), collections.defaultdict(int), collections.defaultdict(list), []
        for x, y in pairs: 
            u.union(x, y)
        for i in range(len(s)):
            groups[u.find(i)].append(s[i])
            graph[i] = u.find(i)
        print(groups)
        print(graph)
        for k in groups.keys():
            groups[k] = collections.deque(sorted(groups[k]))
        return \"\".join([groups[graph[i]].popleft() for i in range(len(s))]) 
            
        
