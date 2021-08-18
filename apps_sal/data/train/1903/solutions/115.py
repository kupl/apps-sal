class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def buildmst(graph, starting_vertex):
            mst = defaultdict(set)
            visited = set([starting_vertex])
            edges = [
                (cost, starting_vertex, to)
                for to, cost in list(graph[starting_vertex].items())
            ]
            heapq.heapify(edges)

            while edges:
                cost, frm, to = heapq.heappop(edges)
                if to not in visited:
                    visited.add(to)
                    mst[frm].add(to)
                    for to_next, cost in list(graph[to].items()):
                        if to_next not in visited:
                            heapq.heappush(edges, (cost, to, to_next))

            return mst

        graph = defaultdict(dict)

        for x in points:
            t = (x[0], x[1])
            for y in points:
                if x != y:
                    graph[t][(y[0], y[1])] = abs(x[0] - y[0]) + abs(x[1] - y[1])

        mst = dict(buildmst(graph, (points[0][0], points[0][1])))
        ans = 0

        for k, v in list(mst.items()):
            for p in v:
                ans += abs(k[0] - p[0]) + abs(k[1] - p[1])

        return ans
