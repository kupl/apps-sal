class Solution:
    import heapq
    import collections
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        min_node = -1
        min_val = float(\"inf\")

        graph = collections.defaultdict(list)
        for s, e, d in edges:
            graph[s].append((e, d))
            graph[e].append((s, d))

        for node in range(n):
            pq = [(0, node)]
            seen = set()
            seen.add(node)

            while pq:
                td, name = heapq.heappop(pq)
                seen.add(name)
                for nex, do in graph[name]:
                    if do + td <= distanceThreshold and nex not in seen:
                        heapq.heappush(pq, (do + td, nex))

            count = len(seen)

            if count <= min_val:
                min_node = node
                min_val = count

        return min_node

