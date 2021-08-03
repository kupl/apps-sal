import numpy as np
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # pre-processing, adjacency matrix for cost of edges;
        if len(points) > 1:
            edge_cost = []
            for i in range(len(points)):
                for j in range(i+1, len(points)):
                    edge_cost.append((i, j, abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])))

            # now try to find the smallest edge to add, find more points to add. 

            edge_cost.sort(key=lambda x: x[2])

            # print(edge_cost)

            connected_component = set()

            min_cost = 0

            i = 0
            
    #         # when some element is not connectected
            while len(connected_component) < len(points):
                i = 0
                while not ((edge_cost[i][0] in connected_component) ^ (edge_cost[i][1] in connected_component)) and len(connected_component)!= 0:
                    i += 1
                if i < len(edge_cost):
                    current = edge_cost[i]
                    min_cost += current[2]
                    connected_component.add(current[0])
                    connected_component.add(current[1])
                    edge_cost.pop(i)
                    # print(\"connected component: %s\" % connected_component)
                else:
                    print(\"Should never be here!\")
            return min_cost
        else:
            return 0
