class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
        
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        UF = UnionFind(len(s))
        res = []
        for x, y in pairs:
            UF.union(x, y)
        parent_to_heap = collections.defaultdict(list)
        for i, p in enumerate(UF.parents):
            heapq.heappush(parent_to_heap[UF.find(p)], s[i])
        for i, p in enumerate(UF.parents):
            res.append(heapq.heappop(parent_to_heap[UF.find(p)]))
        return ''.join(res)
