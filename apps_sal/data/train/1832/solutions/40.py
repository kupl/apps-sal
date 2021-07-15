class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = defaultdict(dict)
        for i, j, w in edges:
            graph[i][j] = w
            graph[j][i] = w
        
        seen = set()
        edges_utilized = Counter()
        h = [(0, 0)]
        while h:
            dist, node = heapq.heappop(h)
            seen.add(node)
            for nbr, w in graph[node].items():
                if nbr not in seen and dist + w + 1 <= M:
                    heapq.heappush(h, (dist + w + 1, nbr))
                edges_utilized[node, nbr] = max(edges_utilized[node, nbr], M - dist)
        
        count = len(seen)
        all_utilized_edges = edges_utilized.keys()
        edges_covered = set()
        for fro, to in all_utilized_edges:
            e = min(fro, to), max(fro, to)
            if e in edges_covered:
                continue
            edges_covered.add(e)
            count += min(graph[fro][to], edges_utilized[fro, to] + edges_utilized[to, fro])
        
        return count
