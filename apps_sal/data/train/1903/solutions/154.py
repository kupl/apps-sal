import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        # mst?
        np = len(points)
        rest = set(range(np))
        cur_val = 0
        rest.remove(cur_val)
        
        def get_costs(rest, node):
            return [(abs(points[node][0] - points[tmp][0]) + abs(points[node][1] - points[tmp][1]), node, tmp) for tmp in rest if tmp != node]
        
        q = get_costs(rest, cur_val)
        heapq.heapify(q)
        
        cost = 0
        
        while len(rest) > 0:
            dist, node1, node2 = heapq.heappop(q)
            if node2 in rest:
                cost += dist
                rest.remove(node2)
                for rsti in get_costs(rest, node2):
                    heapq.heappush(q, rsti)
                    
        return cost

