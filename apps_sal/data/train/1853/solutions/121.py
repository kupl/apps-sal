class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = collections.defaultdict(list)
        for f, t, w in edges:
            g[f].append((t, w))
            g[t].append((f, w))
        
        def bfs(i):
            q = [(0, i)]
            visited = {i}
            while q:
                w, j = heapq.heappop(q)
                visited.add(j)
                for k, w_ in g[j]:
                    if k not in visited and w + w_ <= distanceThreshold:
                        heapq.heappush(q, (w + w_, k))
            return visited
        
        return -min([(len(bfs(i)), -i) for i in range(n)])[1]
