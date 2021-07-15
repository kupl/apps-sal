from heapq import heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        costs = sorted([(self.get_dist(points[i], points[j]), i, j) for i in range(n) for j in range(i)])
        groups = list(range(n))
        def find(node):
            while node != groups[node]:
                node = groups[node]
            return node
        
        res = 0
        for cost, u, v in costs:
            root1, root2 = find(u), find(v)
            if root1 != root2:
                res += cost
                groups[max(root1, root2)] = min(root1, root2)
                
        return res
        
    
    def get_dist(self, pt1, pt2):
        return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])
