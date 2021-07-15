class Solution:
    def minCostConnectPoints(self, A: List[List[int]]) -> int:
        N = len(A)
        P = [i for i in range(N)]                     
        E = []
        for u in range(N):
            x1, y1 = A[u]
            for v in range(u + 1, N):
                x2, y2 = A[v]
                w = abs(x1 - x2) + abs(y1 - y2)
                E.append([ u, v, w ])                   
        E.sort(key = lambda edge: edge[2])              
        def find(x):
            P[x] = P[x] if P[x] == x else find(P[x])
            return P[x]
        def union(a, b):
            a = find(a)
            b = find(b)
            if a == b:
                return False
            P[a] = b                                    
            return True
        return sum([w for u, v, w in E if union(u, v)])
