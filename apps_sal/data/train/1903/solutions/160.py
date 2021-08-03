class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        Prim's algorithm
        Start from some initial point, we build a tree. We track connected points in 'seen'.
        For current point, we add all its edges to a min-heap. Each time, we pickup smallest
        edge which connects to a point not in 'seen'. Repeat until all points are in 'seen'.

        Time: O(V^2 + E*logE)
        Space: O(E)
        '''
        n = len(points)
        seen = set()
        heap = [[0, 0]]
        cost = 0
        for _ in range(n):
            while heap and heap[0][1] in seen:
                heapq.heappop(heap)
            dist, i = heapq.heappop(heap)
            cost += dist
            seen.add(i)
            for j in range(n):
                if j in seen:
                    continue
                dist2j = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(heap, [dist2j, j])

        return cost
