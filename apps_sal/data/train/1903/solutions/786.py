import heapq
class Solution:
    def minCostConnectPoints(self, P: List[List[int]]) -> int:
        def cruskal(nds, E):
            def find(x):
                if p[x] == x: return x
                p[x] = find(p[x])
                return p[x]
            
            p=[i for i in range(nds)]
            ans =0
            while E:
                c, u, v = heapq.heappop(E)
                p_u =find(u)
                p_v =find(v)
                if p_u != p_v:
                    p[p[v]] = p[u]
                    ans+= c
            return ans
        cost = []
        heapq.heapify(cost)
        for i, [x, y] in enumerate(P):
            for j in range(i+1, len(P)):
                x1, y1 = P[j]
                if j ==i: continue
                else: heapq.heappush(cost, (abs(x-x1)+abs(y-y1), i, j))
        #print(len(cost))
        return cruskal(len(P), cost)

