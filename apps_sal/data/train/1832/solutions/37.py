import collections


class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = collections.defaultdict(dict)
        for i, j, w in edges:
            graph[i][j] = graph[j][i] = w
        # min queue for dijastra (distance from source, vertex)
        pq = [(0, 0)]
        # weight used from u to v
        used = {}
        # min distance from source
        dist = {0: 0}
        res = 0

        while pq:
            d, v = heapq.heappop(pq)
            # dist in this path greater than previous route, no need to searching
            if d > dist[v]:
                continue
            # count this vertex
            res += 1

            for nei, weight in list(graph[v].items()):
                # insert how much weight/nodes can be used in edge v->nei
                use_wei = min(weight, M - d)
                used[v, nei] = use_wei

                # get min dis to next node
                d_min = d + weight + 1
                # if next node is not visited and distance smaller than M + 1
                # or has been visited but has greater distance from source
                # we can update distance and push new vertex to heap
                if d_min < dist.get(nei, M + 1):
                    dist[nei] = d_min
                    heapq.heappush(pq, (d_min, nei))

        # insert traveled mid nodes to res
        for i, j, w in edges:
            res += min(w, used.get((i, j), 0) + used.get((j, i), 0))
        return res
