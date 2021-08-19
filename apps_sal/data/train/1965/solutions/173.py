from collections import defaultdict
from heapq import heappush, heappop


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        aj = [defaultdict(set) for i in range(4)]
        total = len(edges)
        for (t, i, j) in edges:
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
            (w, i, j) = heappop(heap)
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
            (w, i, j) = heappop(heap)
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
