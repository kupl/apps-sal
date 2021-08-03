class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], limit: int) -> int:
        graph = collections.defaultdict(lambda: [])
        for n1, n2, w in edges:
            graph[n1].append((n2, w))
            graph[n2].append((n1, w))

        def dijkstra(s):
            ret = 0
            dist = [float('inf')] * n
            dist[s] = 0
            heap = [(0, s)]
            seen = set()
            while heap:
                cur_w, cur = heapq.heappop(heap)
                if cur in seen:
                    continue
                seen.add(cur)

                ret += 1
                for node, w in graph[cur]:
                    if dist[node] > cur_w + w:
                        dist[node] = cur_w + w
                        if dist[node] <= limit:
                            heapq.heappush(heap, (dist[node], node))
            return ret - 1

        return sorted([i for i in range(n)], key=lambda x: [dijkstra(x), -x])[0]
