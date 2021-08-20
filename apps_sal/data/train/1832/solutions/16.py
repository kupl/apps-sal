from heapq import heapify, heappop, heappush


class Solution:

    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        adj = {}
        for (i, j, n) in edges:
            for (n1, n2) in ((i, j), (j, i)):
                adj[n1] = adj.get(n1, {})
                adj[n1][n2] = n
        if 0 not in adj:
            return 1
        length = [M + 1 for _ in range(N)]
        visited = set([0])
        length[0] = 0
        closest = [(e + 1, 0, j) for (j, e) in list(adj[0].items())]
        heapify(closest)
        while closest:
            (l, frm, to) = heappop(closest)
            if l > M:
                break
            if to in visited:
                continue
            length[to] = length[frm] + adj[frm][to] + 1
            visited.add(to)
            for (to2, e) in list(adj.get(to, {}).items()):
                if to2 in visited:
                    continue
                heappush(closest, (length[to] + e + 1, to, to2))
        reach = sum((l <= M for l in length))
        visited = set()
        for (i, l) in enumerate(length):
            visited.add(i)
            for (j, e) in list(adj.get(i, {}).items()):
                if j in visited:
                    continue
                inter = max(min(2 * M - min(length[i], M) - min(length[j], M), e), 0)
                reach += inter
        return reach
