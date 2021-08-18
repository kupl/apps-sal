class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        length = len(points)
        if length < 2:
            return 0

        dist = [[0] * len(points) for _ in range(len(points))]
        value = float('inf')

        for i in range(length):
            dist[i][i] = float('inf')
            for j in range(length):
                if i != j:
                    dist[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                if dist[i][j] < value:
                    value = dist[i][j]
                    idx_i, idx_j = i, j

        connected, result = set([idx_i, idx_j]), dist[idx_i][idx_j]

        heap_q = []

        def increaseQ(heap_q: List[int], idx: int, connected: Set[int]):
            for j in range(length):
                if j not in connected:
                    heapq.heappush(heap_q, (dist[idx][j], idx, j))

        increaseQ(heap_q, idx_i, connected)
        increaseQ(heap_q, idx_j, connected)

        while len(connected) < length:
            v, idx_i, idx_j = heapq.heappop(heap_q)
            if idx_i not in connected:
                connected.add(idx_i)
                increaseQ(heap_q, idx_i, connected)
                result += v
            if idx_j not in connected:
                connected.add(idx_j)
                increaseQ(heap_q, idx_j, connected)
                result += v
        return result
