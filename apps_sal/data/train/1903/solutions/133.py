class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Minimum spanning tree
        # Prim's algorithm

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        ans = 0
        d = collections.defaultdict(list)

        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                # don't use list slicing because the index j will not be the index for the full points list
                if i != j:
                    cost = dist(p1, p2)
                    d[i].append((cost, j))
                    d[j].append((cost, i))

        heap = d[0]
        # heap is a list of costs in ascending order for a given point p1
        heapq.heapify(heap)
        n = len(points)
        visited = [0] * n
        visited[0] = 1
        count = 1

        while heap:
            cost, j = heapq.heappop(heap)
            # ensure cycles are not formed
            if not visited[j]:
                # not yet visit p2 where cost is minimum, can connect p1 and p2
                visited[j] = 1
                count += 1
                ans += cost
                for item in d[j]:
                    # since p1 and p2 are now connected, focus on p2
                    # push items in dict at p2 to heap
                    heapq.heappush(heap, item)

            if count >= n:
                # already connected all points
                break

        return ans

        # # solution
        # manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        # n, c = len(points), collections.defaultdict(list)
        # for i in range(n):
        #     print(\"i: \", i)
        #     for j in range(i+1, n):
        #         print(\"j:\", j)
        #         d = manhattan(points[i], points[j])
        #         c[i].append((d, j))
        #         c[j].append((d, i))
        # cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
        # visited[0] = 1
        # heapq.heapify(heap)
        # while heap:
        #     d, j = heapq.heappop(heap)
        #     if not visited[j]:
        #         visited[j], cnt, ans = 1, cnt+1, ans+d
        #         for record in c[j]: heapq.heappush(heap, record)
        #     if cnt >= n: break
        # return ans
