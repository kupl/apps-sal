# Solve Leetcode 1584. Min Cost to Connect All Points using the boilerplate code below, and then implement Kruskal's algorithm to solve the problem. Use self.distance(pointA, pointB) to find distance (weight of edge) between two nodes.

class DisjointSet:
    def __init__(self, points):
        self.parent = {}
        self.rank = {}
        for point in points:
            self.parent[point] = point
            self.rank[point] = 1

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)

        if self.rank[x_set] < self.rank[y_set]:
            self.parent[x_set] = y_set
        elif self.rank[x_set] > self.rank[y_set]:
            self.parent[y_set] = x_set
        else:
            self.parent[x_set] = y_set
            self.rank[y_set] += 1

        
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        points = [tuple(point) for point in points]
        disjoint_set = DisjointSet(points)
    
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distance = self.distance(points[i], points[j])
                edges.append((distance, points[i], points[j]))
        
        edges.sort()
        answer = 0
        times = 0
        for distance, nodeA, nodeB in edges:
            if disjoint_set.find(nodeA) != disjoint_set.find(nodeB):
                disjoint_set.union(nodeA, nodeB)
                answer += distance
                times += 1
            if times == len(points)-1:
                return answer
        return answer
        
        


    def distance(self, pointA, pointB):
        return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])
