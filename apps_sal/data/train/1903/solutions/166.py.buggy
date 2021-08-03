class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        X = [[None] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                X[i][j] = X[j][i] = abs(points[i][0] - points[j][0]) + \\
                                    abs(points[i][1] - points[j][1])
        
        V = [0] + [float(\"inf\")] * (n - 1)
        S = [True] * n
        
        for _ in range(n - 1):
            i, v = -1, float(\"inf\")
            for j in range(n):
                if S[j] and V[j] < v:
                    i, v = j, V[j]
            
            S[i] = False
            for j in range(n):
                if S[j] and X[i][j] < V[j]:
                    V[j] = X[i][j]    
        
        return sum(V)
