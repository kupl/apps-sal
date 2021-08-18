class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]

        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot:
                return
            parent[xroot] = yroot

        l = len(points)
        parent = [i for i in range(l)]
        dis = []
        for i in range(l):
            for j in range(i + 1, l):
                dis.append(
                    (abs(points[j][1] - points[i][1]) + abs(points[j][0] - points[i][0]), i, j)
                )

        heapq.heapify(dis)
        count = 0
        ans = 0
        while dis:
            temp, node1, node2 = heapq.heappop(dis)
            if find(node1) != find(node2):
                union(node1, node2)
                ans += temp
                count += 1
            if count == l - 1:
                break
        return ans
