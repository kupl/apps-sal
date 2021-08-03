from collections import defaultdict, deque


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = defaultdict(set)
        for src, dest in edges:
            graph[src].add(dest)
            graph[dest].add(src)

        q = deque([[1, 1.0, 0]])
        visited = set()
        while q:
            node, prob, time_step = q.popleft()
            visited.add(node)

            if time_step >= t:
                if node == target:
                    return prob
                continue

            neighbors = graph[node] - visited
            nxt_prob = prob / max(len(neighbors), 1)
            for child in neighbors or [node]:
                q.append((child, nxt_prob, time_step + 1))

        return 0.0
