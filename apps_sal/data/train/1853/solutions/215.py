class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        connect = defaultdict(dict)
        ansheap = []
        for a, b, c in edges:
            connect[a][b] = c
            connect[b][a] = c
        for i in range(n):
            dist = {}
            heap = [(0, i)]
            while heap:
                d, u = heapq.heappop(heap)
                if d > distanceThreshold:
                    break
                if u not in dist:
                    dist[u] = d
                    for v in connect[u]:
                        heapq.heappush(heap, (d + connect[u][v], v))
            heapq.heappush(ansheap, (len(dist), -i))
        return - ansheap[0][1]
