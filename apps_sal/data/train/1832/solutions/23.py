class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        costs = defaultdict(dict)
        for i, j, c in edges:
            costs[i][j] = c
            costs[j][i] = c
        visited = set()
        spans = defaultdict(int)  # (i, j): inner_nodes_visited, i < j
        q = [(0, 0)]  # total_cost, node
        while q:
            dist, a = heapq.heappop(q)
            if a in visited:
                continue
            visited.add(a)
            cons = costs[a]
            for b, cost in list(cons.items()):
                if dist + cost + 1 <= M:
                    heapq.heappush(q, (dist + cost + 1, b))
                spk = (min(a, b), max(a, b))
                spans[spk] = min(spans[spk] + M - dist, cost)
        return len(visited) + sum(spans.values())
