class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UF(n)
        for pair in pairs:
            uf.union(pair[0], pair[1])
        
        groups = collections.defaultdict(list)
        for i in range(n):
            r = uf.root(i)
            groups[r].append(i)
        
        res = ['' for _ in range(n)]
        for r, group in list(groups.items()):
            if len(group) == 1:
                res[r] = (s[group[0]])
            else:
                temp = [s[i] for i in group]
                temp.sort()
                for index, idx in enumerate(sorted(group)):
                    res[idx] = temp[index]
        return ''.join(res)
    
class UF:
    def __init__(self, n):
        self.parents = list(range(n))
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parents[px] = py
    
    def root(self, x):
        return self.find(x)

