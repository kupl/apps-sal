class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        g = [defaultdict(list), defaultdict(list)]
        for i, edges in enumerate([red_edges, blue_edges]):
            for u, v in edges:
                g[i][u].append(v)
        dist = [[0] + [float('inf')] * (n-1) for _ in range(2)]
        for i in range(2):
            q = deque([(0, 0, i)])
            while q:
                d, u, color = q.popleft()
                if d > dist[color][u]:
                    continue
                dist[color][u] = d
                d += 1
                color ^= 1
                for v in g[color][u]:
                    if dist[color][v] > d:
                        q.append([d, v, color])
        return [x if (x := min(a, b)) != float('inf') else -1  for a, b in zip(*dist)]
