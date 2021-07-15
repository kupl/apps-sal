class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjl = [[] for _ in range(n)]
        d = distanceThreshold
        for e in edges:
            i, j, w = e
            adjl[i].append((w, j))
            adjl[j].append((w, i))
        inf = float('inf')
        minc = 1e9
        mini = 0
        for i in range(n):
            ds = [inf for _ in range(n)]
            ds[i] = 0
            fringe = [(e[0], (i, e[1])) for e in adjl[i]]
            heapq.heapify(fringe)
            visited = {i}
            while len(fringe) > 0:
                w, uv = heapq.heappop(fringe)
                u, v = uv
                if w > d:
                    continue
                if v not in visited:
                    ds[v] = min(ds[v], w)
                    for e in adjl[v]:
                        heapq.heappush(fringe, (e[0] + ds[v], (v, e[1])))
                    visited.add(v)
            cnt = len([c for c in ds if c <= d])
            if cnt <= minc:
                minc = cnt
                mini = i
        return mini

