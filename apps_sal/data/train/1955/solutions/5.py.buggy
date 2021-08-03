import heapq
from copy import copy, deepcopy
class MaxHeapObj(object):
    def __init__(self, val): self.val = val
    def __lt__(self, other): return self.val > other.val
    def __eq__(self, other): return self.val == other.val
    def __str__(self): return str(self.val)
 
class MinHeap(object):
    def __init__(self, arr=[]):
        self.h = deepcopy(arr)
        heapq.heapify(self.h)
 
    def heappush(self, x): heapq.heappush(self.h, x)
    def heappop(self): return heapq.heappop(self.h)
    def __getitem__(self, i): return self.h[i]
    def __len__(self): return len(self.h)
 
class MaxHeap(object):
    def __init__(self, arr=[]):
        self.h = [MaxHeapObj(x) for x in arr]
        heapq.heapify(self.h)
 
    def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))
    def heappop(self): return heapq.heappop(self.h).val
    def __getitem__(self, i): return self.h[i].val
    def __len__(self): return len(self.h)

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        res, n, adj, component_num, curr, comp_vals = [], len(s), defaultdict(list), defaultdict(lambda: -1), 0, defaultdict(lambda: MinHeap())
        for edge in pairs:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        def DFS(i, comp):
            
            component_num[i] = comp 
            for j in adj[i]:
                if component_num[j] == -1: DFS(j, comp)
        
        for i in range(n):
            if component_num[i] == -1: 
                DFS(i, curr)
                curr += 1 
            comp_vals[component_num[i]].heappush(s[i])
        
        for i in range(n):
            res.append(comp_vals[component_num[i]].heappop())
        
        return \"\".join(res)
