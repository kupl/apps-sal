class Solution:

    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        to_edges = defaultdict(list)
        for [so, ta] in edges:
            to_edges[so].append(ta)
            to_edges[ta].append(so)
        to_edges[1].append(1)
        queue = deque([(1, 0, 1)])
        visited = {1}
        while queue:
            (node, time, frac) = queue.popleft()
            if node == target:
                if time == t or (time < t and len(to_edges[node]) == 1):
                    return 1 / frac
            if time > t:
                return 0
            for nei in to_edges[node]:
                if nei not in visited:
                    queue.append((nei, time + 1, frac * (len(to_edges[node]) - 1)))
                    visited.add(nei)
        return 0
