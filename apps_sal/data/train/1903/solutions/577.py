class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        if len(points) <= 1:
            return 0

        def dist(a, b):
            return abs(a[1] - b[1]) + abs(a[0] - b[0])

        A = {i: {i} for i in range(len(points))}
        edges = [(dist(p1, p2), i, j) for i, p1 in enumerate(points) for j, p2 in enumerate(points) if p1 != p2]
        import heapq
        heapq.heapify(edges)

        tot = 0
        n = len(points) - 1
        while n:
            w, a, b = heapq.heappop(edges)
            if not A[a].intersection(A[b]):
                # print(\"edge:\",points[a],points[b])
                # print(\"a's set:\" ,A[a])
                # print(\"b's set:\", A[b])
                B = A[a].union(A[b])
                for b in B:
                    A[b] = B
                tot += w
                n -= 1
        print((A[0], len(points)))
        return tot
