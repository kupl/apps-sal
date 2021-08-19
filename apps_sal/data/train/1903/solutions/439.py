from queue import PriorityQueue
import math


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Get lengths of edges, put into Priority Queue
        #         q = PriorityQueue()
        #         for i, point1 in enumerate(points):
        #             for j, point2 in enumerate(points):
        #                 if i == j: continue
        #                 dist = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        #                 q.put((dist, (i, j)))

        q = []
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i + 1, len(points)):
                xj, yj = points[j]
                q.append([abs(xi - xj) + abs(yi - yj), i, j])
        q = sorted(q)

        # For each edge in PQ, grab it, check if it forms a cycle in graph
        # If not, add it to the graph.
        # Increment cost.
        # We can check for a cycle with union find algorithm. (basically check parents)
        cost = 0
        self.arr = [-1 for el in range(len(points))]
        for el in q:
            d, p1, p2 = el[0], el[1], el[2]
            cycle = self.isCycle(p1, p2)
            # print(\"cycle\", cycle)
            if not cycle:
                cost += d
                # print(\"adding d\", d)
                self.combinePoints(p1, p2)
            else:
                continue
            if self.isDone():
                break
            # print(self.arr)
        return cost

    def isDone(self):
        n_neg = 0
        for val in self.arr:
            if val < 0:
                n_neg += 1
        if n_neg == 1:
            return True
        return False

    def combinePoints(self, p1, p2):
        # Find parent of p1, get size
        # Find parent of p2, get size
        # Whichever is smaller, make the smaller parent point to the larger parent.
        # Update the larger parent by adding the size of the smaller parent (keep negatives)
        parent1, children1 = self.getParent(p1, [])
        # print(p1, parent1)
        size1 = self.arr[parent1]
        parent2, children2 = self.getParent(p2, [])
        size2 = self.arr[parent2]

        # If parent2 is bigger
        if abs(size2) > abs(size1):
            self.arr[parent1] = parent2
            self.arr[parent2] = size2 + size1
            self.updateChildren(children1, parent2)
        else:
            self.arr[parent2] = parent1
            self.arr[parent1] = size2 + size1
            self.updateChildren(children2, parent1)

    def isCycle(self, p1, p2):
        parent1, _ = self.getParent(p1, [])
        parent2, _ = self.getParent(p2, [])
        if parent1 == parent2:
            return True
        else:
            return False

    def getParent(self, p1, children):
        if self.arr[p1] < 0:
            return p1, children
        else:
            children.append(p1)
            return self.getParent(self.arr[p1], children)

    def updateChildren(self, children, parent):
        for child in children:
            self.arr[child] = parent
