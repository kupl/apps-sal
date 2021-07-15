class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 0
        n = len(points)
        heap = []
        dic = collections.defaultdict(list)
        #calculate all the distances and put them in a heap
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dic[i].append((dist, j))
                dic[j].append((dist, i))
        #add edges connected to 0 to heap    
        res, count, visited, heap = 0, 0, [0] * n, dic[0]
        visited[0] = 1
        heapq.heapify(heap)
        while heap:
            dist, i = heapq.heappop(heap)
            if not visited[i]:
                res += dist
                count += 1
                visited[i] = 1
                if count == n - 1:
                    return res
                for record in dic[i]:
                    heapq.heappush(heap, record)
    

