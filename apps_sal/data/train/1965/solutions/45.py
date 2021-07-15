# from collections import defaultdict

# class Solution:
#     def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
#         aj = [defaultdict(set) for i in range(4)]
#         total = len(edges)
#         for t, i, j in edges:
#             if i == j:
#                 continue
#             aj[t][i].add(j)
#             aj[t][j].add(i)
        
#         used = set()
#         visited = {1}
#         t3 = [(1, i) for i in aj[3][1]]
#         t1 = [(1, i) for i in aj[1][1]]
#         while len(visited) < n and (t3 or t1):
#             if t3:
#                 i, j = t3.pop()
#                 reusable = True
#             else:
#                 i, j = t1.pop()
#                 reusable = False
#             if j in visited:
#                 continue
                
#             if reusable:
#                 used.add((min(i, j), max(i, j)))
#             visited.add(j)
#             for k in aj[3][j]:
#                 if k not in visited:
#                     t3.append((j, k))
#             for k in aj[1][j]:
#                 if k not in visited:
#                     t1.append((j, k))
#         if len(visited) < n:
#             return -1
            
#         reused = set()
#         visited = {1}
#         t0 = []
#         t2 = [(1, i) for i in aj[2][1]]
#         for i in aj[3][1]:
#             if (1, i) in used:
#                 t0.append((1, i))
#             else:
#                 t2.append((1, i))
#         while len(visited) < n and (t0 or t2):
#             if t0:
#                 i, j = t0.pop()
#                 reusable = True
#             else:
#                 i, j = t2.pop()
#                 reusable = False
#             if j in visited:
#                 continue
                
#             if reusable:
#                 reused.add((min(i, j), max(i, j)))
#             visited.add(j)
#             for k in aj[3][j]:
#                 if k not in visited:
#                     if (min(j, k), max(j, k)) in used:
#                         t0.append((j, k))
#                     else:
#                         t2.append((j, k))
#             for k in aj[2][j]:
#                 if k not in visited:
#                     t2.append((j, k))
#         if len(visited) < n:
#             return -1

#         return total - ((n - 1) * 2 - len(reused))


from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        aj = [defaultdict(set) for i in range(4)]
        total = len(edges)
        for t, i, j in edges:
            if i == j:
                continue
            aj[t][i].add(j)
            aj[t][j].add(i)
        
        reuse = set()
        count = 0
        
        visited = {1}
        heap = []
        for i in aj[3][1]:
            heappush(heap, (1, 1, i))
        for i in aj[1][1]:
            heappush(heap, (2, 1, i))
        while len(visited) < n and heap:
            w, i, j = heappop(heap)
            if j in visited:
                continue
                
            if w == 1:
                reuse.add((i, j))
            count += 1
            visited.add(j)
            for k in aj[3][j]:
                if k not in visited:
                    heappush(heap, (1, j, k))
            for k in aj[1][j]:
                if k not in visited:
                    heappush(heap, (2, j, k))
        if len(visited) < n:
            return -1
            
        visited = {1}
        heap = []
        for i in aj[3][1]:
            if (1, i) in reuse or (i, 1) in reuse:
                heappush(heap, (0, 1, i))
            else:
                heappush(heap, (1, 1, i))
        for i in aj[2][1]:
            heappush(heap, (2, 1, i))
        while len(visited) < n and heap:
            w, i, j = heappop(heap)
            if j in visited:
                continue
                
            if w > 0:
                count += 1
            visited.add(j)
            for k in aj[3][j]:
                if k not in visited:
                    if (j, k) in reuse or (k, j) in reuse:
                        heappush(heap, (0, j, k))
                    else:
                        heappush(heap, (1, j, k))
            for k in aj[2][j]:
                if k not in visited:
                    heappush(heap, (2, j, k))
        if len(visited) < n:
            return -1

        return total - count

