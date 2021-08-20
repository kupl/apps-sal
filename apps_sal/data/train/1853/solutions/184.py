class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = defaultdict(deque)
        for (a, b, d) in edges:
            g[a].append((b, d))
            g[b].append((a, d))

        def helper(node: int, threshold) -> int:
            lookup = {}
            heap = [(0, node)]
            visited = set()
            while heap:
                (d, u) = heapq.heappop(heap)
                if d <= threshold:
                    visited.add(u)
                if d > threshold:
                    return len(visited)
                if u in lookup and lookup[u] < d:
                    continue
                for (v, w) in g[u]:
                    if v not in lookup or (w + d <= threshold and lookup[v] > w + d):
                        lookup[v] = w + d
                        heapq.heappush(heap, (w + d, v))
            return len(visited)
        (min_nei, node) = (float('inf'), None)
        for i in range(n - 1, -1, -1):
            count = helper(i, distanceThreshold)
            if count == 1:
                return i
            if count < min_nei:
                min_nei = count
                node = i
        return node
