class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        res = 0
        for (idx1, point1) in enumerate(points):
            for (idx2, point2) in enumerate(points):
                if idx1 != idx2:
                    man = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
                    graph[idx1].append((man, idx2))
                    graph[idx2].append((man, idx1))
        con = set([0])
        heap = graph[0][:]
        heapify(heap)
        while len(con) != len(points):
            while heap:
                cur = heappop(heap)
                if cur[1] not in con:
                    for neig in graph[cur[1]]:
                        heappush(heap, neig)
                    con.add(cur[1])
                    res += cur[0]
                    break
        return res
