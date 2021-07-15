class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        def dist(points,i,j):
            return abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
        a = collections.defaultdict(list)
        for i in range(n):
            for j in range(i+1,n):
                d = dist(points,i,j)
                a[i].append((d,j))
                a[j].append((d,i))
        ans,cnt,q,visited = 0,1,a[0],[0] * n
        visited[0] = 1
        heapify(q)
        while q:
            d,j = heappop(q)
            if not visited[j]:
                visited[j] = 1
                cnt += 1
                ans += d
                for i in a[j] : heappush(q,i)
            if cnt >= n:
                break
        return ans
