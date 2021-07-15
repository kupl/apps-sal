class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = collections.defaultdict(int)

        def find(p):
            if parent[p] == 0:
                return p
            return find(parent[p])

        def union(p1, p2):
            if p1 != p2:
                if p1 < p2:
                    parent[p2] = p1
                else:
                    parent[p1] = p2

        V = points
        E = []
        for p1 in V:
            for p2 in V:
                if p1 != p2:
                    E.append((tuple(p1),tuple(p2)))
        W = {}
        for edge in E:
            W[edge] = abs(edge[0][0]-edge[1][0]) + abs(edge[0][1]-edge[1][1])
        sorted_W = {k: v for k, v in sorted(W.items(), key=lambda item: item[1])}
    
        count = 0
        cost = 0
        for e in sorted_W:
            x, y = e[0], e[1]
            x_set, y_set = find(x), find(y)
            if x_set != y_set:
                union(x_set, y_set)
                count += 1
                cost += sorted_W[e]
            if count ==  len(V) - 1:
                break
        return cost
