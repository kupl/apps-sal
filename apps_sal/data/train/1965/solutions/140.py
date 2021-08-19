class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        graphs = [collections.defaultdict(list) for _ in range(3)]
        x = [0] * 3
        for (c, i, j) in edges:
            graphs[c - 1][i].append((-c, j))
            graphs[c - 1][j].append((-c, i))
            x[c - 1] += 1
        e = graphs[2][1] + graphs[0][1]
        heapq.heapify(e)
        treeset = set([1])
        ans = 0
        while e:
            (c, y) = heapq.heappop(e)
            if y not in treeset:
                treeset.add(y)
                if c == -3:
                    ans += 1
                for item in graphs[2][y]:
                    heapq.heappush(e, item)
                for item in graphs[0][y]:
                    heapq.heappush(e, item)
        if len(treeset) != n:
            return -1
        e = graphs[2][1] + graphs[1][1]
        heapq.heapify(e)
        treeset = set([1])
        while e:
            (c, y) = heapq.heappop(e)
            if y not in treeset:
                treeset.add(y)
                for item in graphs[2][y]:
                    heapq.heappush(e, item)
                for item in graphs[1][y]:
                    heapq.heappush(e, item)
        if len(treeset) != n:
            return -1
        return len(edges) + ans - 2 * (n - 1)
