import sys


class Solution:

    def manhattan(self, p1, p2):
        cost = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        return cost

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        total_cost = 0
        connected = []
        edges = []
        for i in range(len(points)):
            connected.append(set([i]))
        if len(points) == 1:
            return 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append([i, j, self.manhattan(points[i], points[j])])
        edges = sorted(edges, key=lambda i: i[2])
        edge_counter = 0
        while len(connected) > 1:
            edge = edges[edge_counter]
            edge_counter += 1
            cycle = False
            for tree in connected:
                if edge[0] in tree and edge[1] in tree:
                    cycle = True
                    break
            if cycle == True:
                continue
            else:
                set1 = None
                index1 = None
                set2 = None
                index2 = None
                for i in range(len(connected)):
                    sets = connected[i]
                    if not set1 and edge[0] in sets:
                        set1 = sets
                        index1 = i
                    if not set2 and edge[1] in sets:
                        set2 = sets
                        index2 = i
                    if set1 and set2:
                        break
                connected.append(set1.union(set2))
                del connected[max(index1, index2)]
                del connected[min(index1, index2)]
                total_cost += edge[2]
        return total_cost
