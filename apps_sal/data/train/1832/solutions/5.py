class Solution:

    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = defaultdict(list)
        e2i = {}
        reach = {}
        res = 0
        heap = [(0, 0)]
        hm = {0: 0}
        for (i, (u, v, w)) in enumerate(edges):
            graph[u].append([v, w])
            graph[v].append([u, w])
            e2i[u, v] = i
            e2i[v, u] = i
            reach[i] = 0
        while heap:
            (moves, node) = heapq.heappop(heap)
            if moves > hm[node]:
                continue
            res += 1
            for (nei, cost) in graph[node]:
                idx = e2i[node, nei]
                reach[idx] = min(cost, reach[idx] + M - moves)
                h = moves + cost + 1
                if h < hm.get(nei, M + 1):
                    hm[nei] = h
                    heapq.heappush(heap, (h, nei))
        return res + sum(reach.values())
