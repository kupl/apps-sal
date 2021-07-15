class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:        
        vertices = len(points)
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        for i in range(self.V):
            for j in range(self.V):
                if i == j:
                    self.graph[i][j] = 0
                else:
                    self.graph[i][j]= abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        return self.primMST()

    def minKey(self, key, mstSet):
        min = math.inf
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index
 
    def primMST(self):
        key = [math.inf] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
 
        parent[0] = -1
 
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u       
        res = 0
        for i in range(1, self.V):
            res += self.graph[i][parent[i]]
        return res
