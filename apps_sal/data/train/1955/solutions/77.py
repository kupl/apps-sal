from heapq import heappush, heappop

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def parent(a):
            val, _ = d[a]
            if val == a:
                return a
            return parent(val)
        
        def union(a, b):
            parent1 = parent(a)
            parent2 = parent(b)
            
            if parent1 == parent2:
                return
            
            a, n1 = d[parent1]
            b, n2 = d[parent2]
            if n1 > n2:
                d[b] = (a, n2)
                d[a] = (a, n1 + n2)
            else:
                d[a] = (b, n1)
                d[b] = (b, n1 + n2)
                
        d = [(i, 1) for i in range(len(s))]
        for i, j in pairs:
            union(i, j)
        arrs = [[] for _ in range(len(s))]
        for i in range(len(s)):
            heappush(arrs[parent(i)], s[i])
        sol = list()
        for i in range(len(s)):
            sol.append(heappop(arrs[parent(i)]))
        return ''.join(sol)
        

