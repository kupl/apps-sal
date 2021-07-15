class UnionFind:
    def __init__(self):
        self.roots = {}
        self.depth = {}
    
    def root(self, node):
        if node not in self.roots:
            self.roots[node] = node
            self.depth[node] = 1
        path = []
        while self.roots[node] != node:
            path.append(node)
            node = self.roots[node]
        for elem in path:
            self.roots[elem] = node
        return node

    def connect(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        if self.depth[x] == self.depth[y]:
            new_depth = self.depth[y] + 1
        else:
            new_depth = self.depth[y]
        del self.depth[x]
        self.roots[x] = y
        self.depth[y] = new_depth
        

class Solution:
        
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_span_tree = UnionFind()
        cost = 0
        edges = []
        for i in range(1, len(points)):
            for j in range(i):
                edge_cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([edge_cost, i, j])
        edges.sort()
        to_connect = len(points) - 1
        for edge_cost, i, j in edges:
            if not to_connect:
                break
            if min_span_tree.root(i) != min_span_tree.root(j):
                cost += edge_cost
                min_span_tree.connect(i, j)
                to_connect -= 1
        return cost
