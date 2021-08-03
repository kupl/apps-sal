class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = collections.defaultdict(list)
        res = float('inf')
        min_city = 0
        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))

        def djikstra(node):
            distance = {nid: float('inf') for nid in list(graph.keys())}
            distance[node] = 0
            heap = [(0, node)]
            heapq.heapify(heap)
            total = 0
            while heap:
                d, nd = heapq.heappop(heap)
                if d > distance[nd]:
                    continue
                for nei in graph[nd]:
                    nei_cost, nei_id = nei
                    total = (d + nei_cost)
                    if total < distance[nei_id]:
                        distance[nei_id] = total
                        heapq.heappush(heap, (total, nei_id))
            return sum(dis <= distanceThreshold for dis in list(distance.values())) - 1
        # print(graph.keys())
        res = {djikstra(i): i for i in range(n)}
        return res[min(res)]
