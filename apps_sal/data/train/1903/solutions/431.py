class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uf = {}
        n = len(points)
        rank = [1] * n

        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if rank[px] > rank[py]:
                    px, py = py, px
                rank[py] += rank[px]
                uf[px] = py
                return rank[py] == n
            return False

        hp = [(abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j) for i in range(n) for j in range(i + 1, n)]
        heapq.heapify(hp)
        ans = 0

        while hp:
            d, i, j = heapq.heappop(hp)
            if find(i) != find(j):
                ans += d
                if union(i, j):
                    break

        return ans

        # n = len(points)
        # dist = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        # dic = collections.defaultdict(list)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         d = dist(points[i], points[j])
        #         dic[i].append((d, j))
        #         dic[j].append((d, i))
        # hp = dic[0]
        # heapq.heapify(hp)
        # ans, cnt, seen = 0, 1, [1] + [0] * (n - 1)
        # while hp:
        #     d, i = heapq.heappop(hp)
        #     if not seen[i]:
        #         ans += d
        #         cnt += 1
        #         seen[i] = 1
        #         for j in dic[i]:
        #             heapq.heappush(hp, j)
        #         if cnt == n:
        #             break
        # return ans
