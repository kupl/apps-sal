class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edge_heap = []
        cost_map = {}
        for i, point1 in enumerate(points):
            for j, point2 in enumerate(points):
                if point1 == point2:
                    continue
                cost_map[(min(i, j), max(i,j))] = abs(point1[1] - point2[1]) + abs(point1[0] - point2[0])
        
        forest = set([0])
        for i in range(1, len(points)):
            heapq.heappush(edge_heap, (cost_map[(0, i)], (0, i)))
        
        total_cost = 0
        
        while len(forest) != len(points):
            cost, (v1, v2) = heapq.heappop(edge_heap)
            v1_new = v1 not in forest
            v2_new = v2 not in forest
            if v1_new == v2_new:
                continue
            # print(f\"Adding edge {(points[v1], points[v2])} with cost {cost}\")
            forest.add(v1)
            forest.add(v2)
            total_cost += cost
            
            v_search = v1 if v1_new else v2
            for vx in range(len(points)):
                if vx == v_search or vx in forest:
                    continue
                i, j = min(v_search, vx), max(v_search, vx)
                heapq.heappush(edge_heap, (cost_map[i, j], (i, j)))
            
        return total_cost
