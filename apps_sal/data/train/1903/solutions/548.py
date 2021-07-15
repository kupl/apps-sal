class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        import heapq
        manhattan = lambda a, b:abs(a[0]-b[0]) + abs(a[1]-b[1])
        n, c = len(points), defaultdict(list)
        if n==0:
            return 0
        for i in range(n):
            for j in range(i+1, n):
                dis = manhattan(points[i], points[j])
                c[i].append((dis, j))
                c[j].append((dis, i))
        cnt, ans, visited, heap = 1, 0, [0]*n, c[0]
        visited[0] = 1
        heapq.heapify(heap)
        while cnt<n:
            dis, p = heapq.heappop(heap)
            if not visited[p]:
                visited[p], cnt, ans = 1, cnt+1, ans+dis
                for record in c[p]:
                    heapq.heappush(heap, record)
        return ans 
