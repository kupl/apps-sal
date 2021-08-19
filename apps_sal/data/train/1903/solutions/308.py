class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(roots, x):
            if x != roots[x]:
                roots[x] = find(roots, roots[x])    # compress
            return roots[x]

        n = len(points)
        def manhattan(a, b): return abs(a[0] - b[0]) + abs(a[1] - b[1])
        heap = []
        roots = list(range(n))
        size = [1 for i in range(n)]
        res = 0

        # 先把所有节点按照距离存放到 heap 中
        for i in range(n):
            for j in range(i + 1, n):
                d = manhattan(points[i], points[j])
                heap.append((d, (i, j)))

        # 堆化
        heapq.heapify(heap)

        while heap:
            d, (i, j) = heapq.heappop(heap)
            root1 = find(roots, i)
            root2 = find(roots, j)

            # if root1 != root2:
            #     res += d
            #     # union by rank
            #     if size[root1] < size[root2]:
            #         roots[root1] = root2
            #         size[root2] += size[root1]
            #         if size[root2] == n: break
            #     else:
            #         roots[root2] = root1
            #         size[root1] += size[root2]
            #         if size[root1] == n: break

            if root1 != root2:
                res += d
                # union by rank
                roots[root2] = root1
                size[root1] += size[root2]
                if size[root1] == n:
                    break

        return res
