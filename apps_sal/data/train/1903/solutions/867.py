class DSU: 
    def __init__(self, n): 
        self.p = list(range(n))
        self.r = [0] * n
    def find(self, i): 
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]
    def union(self, i, j): 
        pi, pj = self.find(i), self.find(j)
        if pi != pj: 
            if self.r[pi] >= self.r[pj]: 
                self.p[pj] = pi
                self.r[pi] += (self.r[pi] == self.r[pj])
            else: 
                self.p[pi] = pj
            return True
        return False

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # try minimum spanning treee
        
        to_visit = set(range(1, len(points)))
        pq = [(abs(points[0][0] - points[x][0]) + abs(points[0][1] - points[x][1]), x) for x in range(1, len(points))]
        heapq.heapify(pq)
        ans = 0
        while pq:
            cost, to = heapq.heappop(pq)
            if to in to_visit:
                to_visit.remove(to)
                ans += cost
                for nei in to_visit:
                    x, y = points[nei]
                    heapq.heappush(pq, (abs(x-points[to][0]) + abs(y-points[to][1]), nei))

        return ans
    
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         edges, ans = [], 0
#         for i in range(len(points)):
#             for j in range(i+1, len(points)): 
#                 edges.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
                
#         edges.sort()
#         uf = DSU(len(points))
#         for cost, i, j in edges: 
#             if uf.find(i) != uf.find(j): 
#                 uf.union(i, j)
#                 ans += cost
#         return ans
        
                


