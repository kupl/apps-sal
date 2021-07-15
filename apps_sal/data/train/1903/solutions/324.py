class Node:
    def __init__(self,data,rank,node):        
        self.data = data
        self.rank = rank
        self.node = node            
        self.parent = self

class Solution:
    def minCostConnectPoints(self, a: List[List[int]]) -> int:
        n = len(a)
        if n <= 1: return 0
        d = defaultdict(list)
        min_val, min_i = float('inf'), None        
        for i in range(n-1):            
            for j in range(i+1, n):                
                val = abs(a[i][0]-a[j][0]) + abs(a[i][1]-a[j][1])
                d[i].append((val, i, j)); d[j].append((val, j, i))                         
                if min_val > val: min_val, min_i = val, i
                    
        for i in range(n): heapify(d[i])                
        q = [heappop(d[min_i])]      
        heapify(q)        
        ans, cur = 0, set([min_i])
        while len(cur) < n:            
            val, i, j = heappop(q)
            if j not in cur: ans += val
            cur.add(j)
            while d[i] and d[i][0][2] in cur: heappop(d[i])
            if d[i]: heappush(q, heappop(d[i]))
            while d[j] and d[j][0][2] in cur: heappop(d[j])
            if d[j]: heappush(q, heappop(d[j]))            
        return ans
